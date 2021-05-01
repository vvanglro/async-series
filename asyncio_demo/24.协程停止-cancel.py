# -*- coding: UTF-8 -*-
"""
@author:wanghao
@file:24.协程停止-cancel.py
@time:2021/04/30
"""
import asyncio
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    # 返回事件循环所运行的未完成的 Task 对象的集合
    print(asyncio.all_tasks())

    # 取消Task任务
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())