# W5 第一课：我的第一个 API
# 任务：
#   1. 先原样跑起来，看能不能访问 http://127.0.0.1:8000
#   2. 然后自己加一个 /hello 接口（见文件末尾 TODO）

from fastapi import FastAPI

app = FastAPI(title="我的第一个 API")


@app.get("/")
def root():
    return {"message": "服务跑起来了"}


# ===== TODO：你来写 =====
# 加一个 GET /hello 接口，返回 {"msg": "hello"}
# 提示：照着上面 root 的样子，装饰器改成 @app.get("/hello")，函数名 hello，return 一个字典

# 在这里写你的 /hello 接口
@app.get("/hello")
def hello():
    return {"msg": "hello"}