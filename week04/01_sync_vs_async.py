import time
import asyncio


def task(name, seconds):
    print(f"{name}开始")
    time.sleep(seconds)
    print(f"{name}结束")


start = time.time()
task("烧水", 2)
task("煮饭", 2)
task("洗碗", 2)
print(f"总用时：{time.time() - start:.1f} 秒")

async def task_async(name, seconds):
    print(f"{name}开始")
    await asyncio.sleep(seconds)
    print(f"{name}结束")

async def main():
    start = time.time()
    await asyncio.gather(
        task_async("烧水",2),
        task_async("煮饭",2),
        task_async("洗碗",2)
    )
    print(f"总时长：{time.time()-start:.1f}秒")
asyncio.run(main())
