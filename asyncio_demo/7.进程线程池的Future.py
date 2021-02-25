# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 17:53
# @Author  : wanghao
# @File    : 7.进程线程池的Future.py
# @Software: PyCharm

import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(1)
    print(value)

pool = ThreadPoolExecutor(max_workers=5)
# 或 pool = ProcessPoolExecutor(max_workers=5)
for i in range(10):
    '''
        https://www.cnblogs.com/kangoroo/p/7628092.html
        submit方法用于提交一个可并行的方法，submit方法同时返回一个future实例。
        future对象标识这个线程/进程异步进行，并在未来的某个时间执行完成。future实例表示线程/进程状态的回调。
        
        future
        submit函数返回future对象，future提供了跟踪任务执行状态的方法。比如判断任务是否执行中future.running()，判断任务是否执行完成future.done()等等。
        as_completed方法传入futures迭代器和timeout两个参数
        默认timeout=None，阻塞等待任务执行完成，并返回执行完成的future对象迭代器，迭代器是通过yield实现的。 
        timeout>0，等待timeout时间，如果timeout时间到仍有任务未能完成，不再执行并抛出异常TimeoutError
    '''
    fut = pool.submit(func, i)
    print(fut)