import socket
import sys

from fastapi import FastAPI

app = FastAPI()

hostname = socket.gethostname()

version = f"{sys.version_info.major}.{sys.version_info.minor}"


@app.get("/")
async def read_root():
    return {
        "name": "my-app",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}"
    }
