# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 15:29
# @Author  : wanghao
# @File    : 14.异步操作redis.py
# @Software: PyCharm
'''
当通过python去操作redis时，链接、设置值、获取值 这些都涉及网络IO请求，使用asycio异步的方式可以在IO等待时去做一些其他任务，从而提升性能。

安装Python异步操作redis模块

pip3 install aioredis
'''
# 示例1：异步操作redis。
import asyncio
import aioredis


async def execute(address, password):
    print("开始执行", address)
    # 网络IO操作：创建redis连接
    redis = await aioredis.create_redis(address, password=password)
    # 网络IO操作：在redis中设置哈希值car，内部在设三个键值对，即： redis = { car:{key1:1,key2:2,key3:3}}
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)
    # 网络IO操作：去redis中获取值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)
    redis.close()
    # 网络IO操作：关闭redis连接
    await redis.wait_closed()
    print("结束", address)


asyncio.run(execute('redis://47.93.4.198:6379', "root!2345"))


# 示例2：连接多个redis做操作（遇到IO会切换其他任务，提供了性能）。

async def execute(address, password):
    print("开始执行", address)
    # 网络IO操作：先去连接 47.93.4.197:6379，遇到IO则自动切换任务，去连接47.93.4.198:6379
    redis = await aioredis.create_redis_pool(address, password=password)
    # 网络IO操作：遇到IO会自动切换任务
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)
    # 网络IO操作：遇到IO会自动切换任务
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)
    redis.close()
    # 网络IO操作：遇到IO会自动切换任务
    await redis.wait_closed()
    print("结束", address)


task_list = [
    execute('redis://47.93.4.197:6379', "root!2345"),
    execute('redis://47.93.4.198:6379', "root!2345")
]
asyncio.run(asyncio.wait(task_list))


# 更多redis操作参考aioredis官网：https://aioredis.readthedocs.io/en/v1.3.0/start.html
