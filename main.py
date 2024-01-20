import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.routes import qrcode
from datetime import datetime

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting up!!")
    yield
    print("Server is shutting down!!")

load_dotenv()

app = FastAPI(lifespan=lifespan)

app.include_router(qrcode.router, prefix="/v1/qrcode", tags=["qrcode"])

server_start_time = datetime.now()

@app.get("/", response_class=JSONResponse)
def root():
    return {
        "serviceName": "FastApi Python Service", 
        "message": "Welcome to the Fast API Backend",
        "author": "Aravind Venkatesan",
        "repository": "https://github.com/aravinve/fastapi-backend"
    }

@app.get("/health", response_class=JSONResponse)
def check_health():
    return {"status": "OK"}

@app.get("/readiness", response_class=JSONResponse)
def check_readiness():
    # Add your custom readiness checks here
    # For example, check if your application dependencies are available
    # If everything is ready, return {"status": "OK"}
    return {"status": "OK"}

@app.get("/up", response_class=JSONResponse)
def get_server_uptime():
    server_uptime = datetime.now() - server_start_time
    return {"status": "OK", "uptime": str(server_uptime)}

if __name__ == "__main__":
    host = os.getenv("FASTAPI_HOST", "0.0.0.0")
    port = int(os.getenv("FASTAPI_PORT", 8000))
    print(f"Server using host={host}; port={port};")
    import uvicorn
    uvicorn.run(app, host, port)
