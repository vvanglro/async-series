# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 17:14
# @Author  : wanghao
# @File    : 3.执行协程函数.py
# @Software: PyCharm
import asyncio
async def func():
    print("协程内部代码")

# 调用协程函数，返回一个协程对象。
result = func()

# 方式一
# loop = asyncio.get_event_loop() # 创建一个事件循环
# loop.run_until_complete(result) # 将协程当做任务提交到事件循环的任务列表中，协程执行完成之后终止。

# 方式二
# 本质上方式一是一样的，内部先 创建事件循环 然后执行 run_until_complete，一个简便的写法。
# asyncio.run 函数在 Python 3.7 中加入 asyncio 模块，
asyncio.run(result)