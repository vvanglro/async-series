# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 17:59
# @Author  : wanghao
# @File    : 22.协程的返回结果获取.py
# @Software: PyCharm
import asyncio
import time

async def func(var):
    print('waiting:',var)
    await asyncio.sleep(var)
    return 'Don after {}s'.format(var)


async def main():
    # http://blog.sina.com.cn/s/blog_6262a50e0102wngq.html
    # ensure_future 除了接受 coroutine 作为参数，还接受 future 作为参数
    # create_task 接受 coroutine 作为参数
    # https://www.imooc.com/article/263959
    # asyncio.ensure_future和asyncio.create_task的区别
    # 使用asyncio.create_task时需有事件循环的存在  而asyncio.ensure_future不需要

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
    # results = await asyncio.gather(*task_list)
    # for result in results:
    #     print(result)

    # 3.获取返回结果方式
    # return await asyncio.gather(*task_list)

    # 4.获取返回结果方式
    # return await asyncio.wait(task_list)

    # 5.获取返回结果方式
    for task in asyncio.as_completed(task_list):
        result = await task
        print(result)


if __name__ == '__main__':

    st = time.time()

    # 1 和 2  5的
    asyncio.run(main())

    # 3.获取返回结果方式
    # results = asyncio.run(main())
    # for result in results:
    #     print(result)

    # 4.获取返回结果方式
    # dones, pending= asyncio.run(main())
    # for task in dones:
    #     print(task.result())


    print(time.time()-st)