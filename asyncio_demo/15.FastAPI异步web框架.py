# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 15:31
# @Author  : wanghao
# @File    : 15.FastAPI异步web框架.py
# @Software: PyCharm
'''
FastAPI是一款用于构建API的高性能web框架，框架基于Python3.6+的 type hints搭建。

接下里的异步示例以FastAPI和uvicorn来讲解（uvicorn是一个支持异步的asgi）。

安装FastAPI web 框架，

pip3 install fastapi
安装uvicorn，本质上为web提供socket server的支持的asgi（一般支持异步称asgi、不支持异步称wsgi）

pip3 install uvicorn
'''
import asyncio
import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()
# 创建的redis连接池
REDIS_POOL = aioredis.ConnectionsPool('redis://47.193.14.198:6379', password="root123", minsize=1, maxsize=10)


@app.get("/")
def index():
    """ 普通操作接口 """
    return {"message": "Hello World"}


'''
在有多个用户并发请求的情况下，异步方式来编写的接口可以在IO等待过程中去处理其他的请求，提供性能。

例如：同时有两个用户并发来向接口 http://127.0.0.1:5000/red 发送请求，服务端只有一个线程，同一时刻只有一个请求被处理。 
异步处理可以提供并发是因为：当视图函数在处理第一个请求时，第二个请求此时是等待被处理的状态，当第一个请求遇到IO等待时，会自动切换去接收并处理第二个请求，当遇到IO时自动化切换至其他请求，一旦有请求IO执行完毕，则会再次回到指定请求向下继续执行其功能代码。
'''
@app.get("/red")
async def red():
    """ 异步操作接口 """
    print("请求来了")

    await asyncio.sleep(3)

    # 连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)

    # 设置值
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 读取值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    # 连接归还连接池
    REDIS_POOL.release(conn)

    return result


if __name__ == '__main__':
    # 这里的luffy是py文件的名称 故这里是15.FastAPI异步web框架
    uvicorn.run("luffy:app", host="127.0.0.1", port=5000, log_level="info")
