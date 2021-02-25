# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:30
# @Author  : wanghao
# @File    : 11.异步上下文管理器.py
# @Software: PyCharm
'''
此种对象通过定义 __aenter__() 和 __aexit__() 方法来对 async with 语句中的环境进行控制。由 PEP 492 引入。

'''

import asyncio


class AsyncContextManager:

    def __init__(self):
        self.conn = None

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # 异步关闭数据库链接
        await asyncio.sleep(1)


async def func():
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)


asyncio.run(func())
