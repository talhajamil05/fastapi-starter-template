from fastapi import FastAPI
from src.routers.healthcheck import router as healthcheck_router

app = FastAPI()

app.include_router(healthcheck_router, prefix="/api")
