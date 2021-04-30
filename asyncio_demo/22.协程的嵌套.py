# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 17:59
# @Author  : wanghao
# @File    : 22.协程的嵌套.py
# @Software: PyCharm
import asyncio
import time

async def func(var):
    print('waiting:',var)
    await asyncio.sleep(var)
    return 'Don after {}s'.format(var)


async def main():

    # py3.8可以给任务取名 name参数 在返回的done中可以看见自己取的名
    task_list = [
        asyncio.create_task(func(1), name='func1'),
        asyncio.create_task(func(2), name='func2'),
        asyncio.create_task(func(3), name='func3')
    ]


    # task_list = [
    #     asyncio.ensure_future(func(1)),
    #     asyncio.ensure_future(func(2)),
    #     asyncio.ensure_future(func(3))
    # ]

    #1.获取返回结果的方式
    # done,pending = await asyncio.wait(task_list)
    # for task in done:
    #     # print(dir(task))
    #     # 获取上边设置的name名字
    #     # ？不加task.get_name()时  task.result()返回的顺序和create_task一样
    #     # ？加了task.get_name()时   返回的顺序乱了
    #     print(task.get_name())
    #     print('task 返回结果：', task.result())


    #2.获取返回结果的方式
    results = await asyncio.gather(*task_list)
    for result in results:
        print(result)


st = time.time()
asyncio.run(main())

print(time.time()-st)