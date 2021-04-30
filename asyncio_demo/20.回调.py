# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 16:27
# @Author  : wanghao
# @File    : 20.回调.py
# @Software: PyCharm
import asyncio


async def do_work(var):
    print('waiting:',var)
    return 'Done after {}s'.format(var)

def callback(future):
    print(future)
    print(dir(future))
    print(future.done())
    print('Callback:', future.result())


#获取协程对象
coroutine = do_work(3)

#创建事件循环
loop = asyncio.get_event_loop()
#创建任务
task = loop.create_task(coroutine)

#第一种 给任务添加绑定函数
task.add_done_callback(callback)

loop.run_until_complete(task)

# 第二种 直接调用task中的result来获取返回结果
print('直接获取返回结果：', task.result())