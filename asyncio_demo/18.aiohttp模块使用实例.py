# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 15:43
# @Author  : wanghao
# @File    : 18.aiohttp模块使用实例.py
# @Software: PyCharm
'''
在编写爬虫应用时，需要通过网络IO去请求目标数据，这种情况适合使用异步编程来提升性能，接下来我们使用支持异步编程的aiohttp模块来实现。

安装aiohttp模块
pip install aiohttp
'''
import selectors

import aiohttp
import asyncio


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print("得到结果：", url, len(text))


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://python.org',
            'https://www.baidu.com',
            'https://www.pythonav.com'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    # win下会报错RuntimeError: Event loop is closed 是因为win下py3.8+不支持 https://learnku.com/python/t/43091
    # asyncio.run(main())


    selector = selectors.SelectSelector()
    loop = asyncio.SelectorEventLoop(selector)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
