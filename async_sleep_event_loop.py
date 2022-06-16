from collections import deque
import time
import heapq

# https://mleue.com/posts/yield-to-async-await/


class Timer:
    def __init__(self, delay):
        self._when = time.time() + delay

    def __await__(self):
        yield self

    def __lt__(self, other):
        return self._when < other

    def __le__(self, other):
        return self._when <= other

    def __gt__(self, other):
        return self._when > other

    def __ge__(self, other):
        return self._when >= other


async def sleep(delay):
    await Timer(delay)


async def get_page():
    print("Starting do download page")
    await sleep(1)
    print("Done downloading page")
    return "<html>Hello</html>"


async def write_db(data):
    print("Starting to write data to db")
    await sleep(0.5)
    print("Connected to db")
    await sleep(1)
    print("Done writing data to db")


async def worker():
    page = await get_page()
    await write_db(page)


def scheduler(coros):
    start = time.time()
    ready = deque(coros)
    sleeping = []

    while True:
        if not ready and not sleeping:
            break
        if not ready:
            timer, coro = heapq.heappop(sleeping)
            if timer > time.time():
                 time.sleep(timer._when - time.time())
            ready.append(coro)
        try:
            coro = ready.popleft()
            result = coro.send(None)
            if isinstance(result, Timer):
                heapq.heappush(sleeping, (result, coro))
            else:
                print(f"Got: {result}")
        except StopIteration:
            pass
    print(f"Time elapsed: {time.time() - start:.3}s")


if __name__ == '__main__':
    tasks = []
    for i in range(10):
        tasks.append(worker())
    scheduler(tasks)
