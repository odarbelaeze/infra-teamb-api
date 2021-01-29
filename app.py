import os

from fastapi import FastAPI

app = FastAPI()


@app.get("{path:path}")
async def root(path: str):
    message = os.environ.get("MESSAGE", "set the `MESSAGE` env var to customize")
    host = os.uname().nodename
    return {
        "message": message,
        "path": path,
        "host": host,
    }
