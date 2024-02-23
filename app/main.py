import uvicorn
from fastapi import FastAPI

from apis.v1.reports_endpoints import reports_routers

app = FastAPI(title='KCPF')
app.include_router(reports_routers)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
