# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 17:15
# @Author  : wanghao
# @File    : 4.await.py
# @Software: PyCharm
import asyncio
async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。
    # 当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response = await asyncio.sleep(2)
    print("IO请求结束，结果为：", response)
result = func()
asyncio.run(result)



async def others():
    print("start")
    await asyncio.sleep(2)
    print('end')
    return '返回值'
async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response = await others()
    print("IO请求结束，结果为：", response)
asyncio.run( func() )




import asyncio
async def others():
    print("start")
    await asyncio.sleep(2)
    print('end')
    return '返回值'
async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response1 = await others()
    print("IO请求结束，结果为：", response1)
    response2 = await others()
    print("IO请求结束，结果为：", response2)
asyncio.run( func() )




