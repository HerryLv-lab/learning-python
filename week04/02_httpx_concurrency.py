import asyncio
import time
import httpx

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]


# ===== 同步版：一个接一个抓 =====
def fetch_sync(url):
    r = httpx.get(url, timeout=15)
    return r.status_code


print("===== 同步版 =====")
start = time.time()
for u in URLS:
    print(f"状态码: {fetch_sync(u)}")
print(f"总用时: {time.time() - start:.1f} 秒")


# ===== 异步版：三个同时抓 =====
async def fetch(client, url):
    r = await client.get(url, timeout=15)
    return r.status_code


async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch(client, URLS[0]),
            fetch(client, URLS[1]),
            fetch(client, URLS[2]),
        )
    print(f"状态码: {results}")
    print(f"总用时: {time.time() - start:.1f} 秒")


print("===== 异步版 =====")
asyncio.run(main())
