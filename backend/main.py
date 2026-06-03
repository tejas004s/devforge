from fastapi import FastAPI

from api.workflow import router

app = FastAPI(
    title="DevForge AI",
    version="1.0.0"
)

app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }