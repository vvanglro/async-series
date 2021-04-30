# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 17:04
# @Author  : wanghao
# @File    : 21.asyncio实现并发.py
# @Software: PyCharm
import asyncio,time

async def func(var):
    print('waiting:',var)
    await asyncio.sleep(var)
    return 'Don after {}s'.format(var)

st =time.time()

task_list = [
    asyncio.ensure_future(func(1)),
    asyncio.ensure_future(func(2)),
    asyncio.ensure_future(func(3)),
]

print(task_list)

# http://blog.sina.com.cn/s/blog_6262a50e0102wngq.html
# ensure_future 除了接受 coroutine 作为参数，还接受 future 作为参数
# create_task 接受 coroutine 作为参数
# https://www.imooc.com/article/263959
# asyncio.ensure_future和asyncio.create_task的区别
# 使用asyncio.create_task时需有事件循环的存在  而asyncio.ensure_future不需要

loop = asyncio.get_event_loop()


# task_list = [
#     loop.create_task(func(1)),
#     loop.create_task(func(2)),
#     loop.create_task(func(3)),
# ]
# print(task_list)
loop.run_until_complete(asyncio.wait(task_list))



for task in task_list:
    print(task.result())

print(time.time() - st)