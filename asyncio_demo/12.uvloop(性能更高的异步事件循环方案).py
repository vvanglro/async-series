# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:33
# @Author  : wanghao
# @File    : 12.uvloop(性能更高的异步事件循环方案).py
# @Software: PyCharm
'''
Python标准库中提供了asyncio模块，用于支持基于协程的异步编程。

uvloop是 asyncio 中的事件循环的替代方案，替换后可以使得asyncio性能提高。事实上，uvloop要比nodejs、gevent等其他python异步框架至少要快2倍，性能可以比肩Go语言。

安装uvloop
pip install uvloop
2021年2月7日 暂时不支持windows下用这个库


pip3 install uvloop
在项目中想要使用uvloop替换asyncio的事件循环也非常简单，只要在代码中这么做就行。

import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# 编写asyncio的代码，与之前写的代码一致。
# 内部的事件循环自动化会变为uvloop
asyncio.run(...)
注意：知名的asgi uvicorn内部就是使用的uvloop的事件循环。
'''