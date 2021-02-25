# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 15:38
# @Author  : wanghao
# @File    : 16.基于上下文管理的redis.py
# @Software: PyCharm
'''
基于上下文管理，来实现自动化管理的案例：
'''

# 示例1：redis
import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()
REDIS_POOL = aioredis.ConnectionsPool('redis://47.193.14.198:6379', password="root123", minsize=1, maxsize=10)


@app.get("/")
def index():
    """ 普通操作接口 """
    return {"message": "Hello World"}


@app.get("/red")
async def red():
    """ 异步操作接口 """
    print("请求来了")
    async with REDIS_POOL.get() as conn:
        redis = Redis(conn)
        # 设置值
        await redis.hmset_dict('car', key1=1, key2=2, key3=3)
        # 读取值
        result = await redis.hgetall('car', encoding='utf-8')
        print(result)
    return result


if __name__ == '__main__':
    uvicorn.run("fast3:app", host="127.0.0.1", port=5000, log_level="info")




