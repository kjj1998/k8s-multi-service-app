import logging
import asyncpg
import os

from fastapi import FastAPI, Request, Response
from datetime import datetime, timezone

logger = logging.getLogger("uvicorn")

app = FastAPI()


@app.get("/")
async def root(request: Request):
    DB_HOST = os.getenv("DB_HOST", "localhost") 
    request_time = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    conn = await asyncpg.connect(f"postgresql://postgres:postgres@{DB_HOST}:5432/app")
    await conn.execute(
        "INSERT INTO requests (path, host, port, time) VALUES ($1, $2, $3, $4)",
        request.url.path,
        request.client.host if request.client else "unknown",
        request.client.port if request.client else "unknown",
        request_time,
    )
    await conn.close()

    return {
        "path": request.url.path,
        "host": request.client.host if request.client else "unknown",
        "port": request.client.port if request.client else "unknown",
        "time": request_time,
    }

@app.get("/healthcheck")
async def healthcheck():
    return Response(status_code=200)
