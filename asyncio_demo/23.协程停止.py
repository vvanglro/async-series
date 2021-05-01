# -*- coding: UTF-8 -*-
"""
@author:wanghao
@file:23.协程停止.py
@time:2021/04/30
"""
import asyncio
import time


async def func(var):
    print('waiting:',var)
    await asyncio.sleep(var)
    return 'Don after {}s'.format(var)



tasks = [
    func(1),
    func(2),
    func(3),
]

st = time.time()

# asyncio.run(asyncio.wait(tasks))

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    # 获取事件循环中所有任务列表
    # print(asyncio.all_tasks(loop))
    for task in asyncio.all_tasks(loop):
        print(task)
        print(task.cancel())  #如果返回的True代表当前任务取消成功
        print(task)
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print(time.time() -st)