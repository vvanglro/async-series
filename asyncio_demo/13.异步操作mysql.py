# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 15:26
# @Author  : wanghao
# @File    : 13.异步操作mysql.py
# @Software: PyCharm
'''
当通过python去操作MySQL时，连接、执行SQL、关闭都涉及网络IO请求，使用asycio异步的方式可以在IO等待时去做一些其他任务，从而提升性能。

安装Python异步操作redis模块

pip3 install aiomysql
'''

# 示例1：

import asyncio
import aiomysql


async def execute():
    # 网络IO操作：连接MySQL
    conn = await aiomysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='mysql', )
    # 网络IO操作：创建CURSOR
    cur = await conn.cursor()
    # 网络IO操作：执行SQL
    await cur.execute("SELECT Host,User FROM user")
    # 网络IO操作：获取SQL结果
    result = await cur.fetchall()
    print(result)
    # 网络IO操作：关闭链接
    await cur.close()
    conn.close()


asyncio.run(execute())


# 示例2：

async def execute(host, password):
    print("开始", host)
    # 网络IO操作：先去连接 47.93.40.197，遇到IO则自动切换任务，去连接47.93.40.198:6379
    conn = await aiomysql.connect(host=host, port=3306, user='root', password=password, db='mysql')
    # 网络IO操作：遇到IO会自动切换任务
    cur = await conn.cursor()
    # 网络IO操作：遇到IO会自动切换任务
    await cur.execute("SELECT Host,User FROM user")
    # 网络IO操作：遇到IO会自动切换任务
    result = await cur.fetchall()
    print(result)
    # 网络IO操作：遇到IO会自动切换任务
    await cur.close()
    conn.close()
    print("结束", host)


task_list = [
    execute('47.93.40.197', "root!2345"),
    execute('47.93.40.197', "root!2345")
]
asyncio.run(asyncio.wait(task_list))
