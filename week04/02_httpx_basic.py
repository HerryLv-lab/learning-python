# 任务：用 httpx 访问 https://httpbin.org/get，打印状态码
# 1. import httpx
# 2. r = httpx.get(网址, timeout=10)
# 3. print(r.status_code)
# 预期输出：200

# 在这里写你的代码
import httpx
import asyncio

r = httpx.get("http://httpbin.org/headers",timeout=10)
print(r.status_code)

async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get("http://httpbin.org/headers",timeout=10)
    print(r.status_code)
asyncio.run(main())