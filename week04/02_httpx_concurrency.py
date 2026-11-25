# W4 台阶3：同步 vs 异步 并发对比（重写版）
# 目标：抓 3 个 https://httpbin.org/delay/1（每个故意延迟 1 秒），对比总用时
# 预期：同步 ≈5.5 秒，异步 ≈2 秒
#
# 【规则】一次只做一步，每步跑通再往下。不要一次全写完。
#
# 步1 同步版：
#   - 先 start = time.time()
#   - for u in URLS: 里用 httpx.get(u, timeout=15)，打印状态码
#   - 最后打印总用时 → 预期 5.5 秒左右
#
# 步2 异步取一个：
#   - async def fetch(client, url): 里 r = await client.get(url, timeout=15)，return r.status_code
#   - async def main(): 用 async with httpx.AsyncClient() as client，只抓 URLS[0]，打印状态码
#
# 步3 三个并发：
#   - main 里把三个 fetch 塞进 asyncio.gather(...)，打印 results
#
# 步4 计时：
#   - 异步版也加 start = time.time()，打印总用时 → 预期 2 秒左右
#
# 步5 点火：最后加 asyncio.run(main())

import time
import asyncio
import httpx

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]


# ===== 步1：同步版（你写） =====
start = time.time()
for u in URLS:
    r = httpx.get(u,timeout=15)
    print(r.status_code)
print(f"同步总用时：{time.time() - start:.1f}秒")

# ===== 步2-4：异步版（你写） =====
async def fetch(client, url):
    r = await client.get(url, timeout=15)
    return r.status_code

async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        status = await asyncio.gather(
            fetch(client, URLS[0]),
            fetch(client, URLS[1]),
            fetch(client, URLS[2]),
        )
        print(status)
        print(type(status))
    print(f"异步总用时：{time.time() - start:.1f}秒")

asyncio.run(main())