from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI(title="个人记账预算管理工具 API")

# 写一个根路由测试一下
@app.get("/")
def read_root():
    return {"message": "Hello, Finance Tracker! 后端服务启动成功！"}