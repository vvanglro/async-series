# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 15:42
# @Author  : wanghao
# @File    : 17.基于上下文管理的mysql.py.py
# @Software: PyCharm
'''
基于上下文管理，来实现自动化管理的案例：
'''

# 示例2：mysql
import asyncio
import uvicorn
from fastapi import FastAPI
import aiomysql

app = FastAPI()
# 创建数据库连接池
pool = aiomysql.Pool(host='127.0.0.1', port=3306, user='root', password='123', db='mysql',
                     minsize=1, maxsize=10, echo=False, pool_recycle=-1, loop=asyncio.get_event_loop())


@app.get("/red")
async def red():
    """ 异步操作接口 """
    # 去数据库连接池申请链接
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            # 网络IO操作：执行SQL
            await cur.execute("SELECT Host,User FROM user")
            # 网络IO操作：获取SQL结果
            result = await cur.fetchall()
            print(result)
            # 网络IO操作：关闭链接
    return {"result": "ok"}


if __name__ == '__main__':
    uvicorn.run("fast2:app", host="127.0.0.1", port=5000, log_level="info")