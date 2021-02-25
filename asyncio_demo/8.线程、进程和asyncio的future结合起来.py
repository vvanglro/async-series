# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 18:00
# @Author  : wanghao
# @File    : 8.线程、进程和asyncio的future结合起来.py
# @Software: PyCharm
'''
两个Future对象是不同的，他们是为不同的应用场景而设计，例如：concurrent.futures.Future不支持await语法 等。

官方提示两对象之间不同：

unlike asyncio Futures, concurrent.futures.Future instances cannot be awaited.

asyncio.Future.result() and asyncio.Future.exception() do not accept the timeout argument.

asyncio.Future.result() and asyncio.Future.exception() raise an InvalidStateError exception when the Future is not done.
Callbacks registered with asyncio.Future.add_done_callback() are not called immediately. They are scheduled with loop.call_soon() instead.
asyncio Future is not compatible with the concurrent.futures.wait() and concurrent.futures.as_completed() functions.
在Python提供了一个将futures.Future 对象包装成asyncio.Future对象的函数 asynic.wrap_future。

接下里你肯定问：为什么python会提供这种功能？

其实，一般在程序开发中我们要么统一使用 asycio 的协程实现异步操作、要么都使用进程池和线程池实现异步操作。但如果 协程的异步和 进程池/线程池的异步 混搭时，那么就会用到此功能了。
'''

import time
import asyncio
import concurrent.futures

def func1():
    # 某个耗时操作
    time.sleep(2)
    return "SB"

async def main():
    loop = asyncio.get_running_loop()

    # 1. Run in the default loop's executor ( 默认ThreadPoolExecutor )
    # 第一步：内部会先调用 ThreadPoolExecutor 的 submit 方法去线程池中申请一个线程去执行func1函数，并返回一个concurrent.futures.Future对象
    # 第二步：调用asyncio.wrap_future将concurrent.futures.Future对象包装为asycio.Future对象。
    # 因为concurrent.futures.Future对象不支持await语法，所以需要包装为 asycio.Future对象 才能使用。

    fut = loop.run_in_executor(None, func1) # 这里None默认为线程池 和下边第二种方法一样
    result = await fut
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, func1)
    #     print('custom thread pool', result)

    # 3. Run in a custom process pool:
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, func1)
    #     print('custom process pool', result)
asyncio.run(main())