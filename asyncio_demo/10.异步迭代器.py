# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:28
# @Author  : wanghao
# @File    : 10.异步迭代器.py
# @Software: PyCharm
'''
什么是异步迭代器

实现了 __aiter__() 和 __anext__() 方法的对象。__anext__ 必须返回一个 awaitable 对象。async for 会处理异步迭代器的 __anext__() 方法所返回的可等待对象，直到其引发一个 StopAsyncIteration 异常。由 PEP 492 引入。

什么是异步可迭代对象？

可在 async for 语句中被使用的对象。必须通过它的 __aiter__() 方法返回一个 asynchronous iterator。由 PEP 492 引入。

'''

import asyncio
class Reader(object):
    """ 自定义异步迭代器（同时也是异步可迭代对象） """

    def __init__(self):
        self.count = 0


    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count


    def __aiter__(self):
        return self


    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration
        return val


async def func():
    # 创建异步可迭代对象
    async_iter = Reader()
    # async for 必须要放在async def函数内，否则语法错误。
    async for item in async_iter:
        print(item)
asyncio.run(func())