import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI, Path, Query, Body, Cookie, Header, Request, Response, status, Form, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import Tag
from datetime import datetime

from src.utils.swagger_tag import SwaggerTag
from src.routes import qrcode

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting up!!")
    yield
    print("Server is shutting down!!")

server_start_time = datetime.now()

load_dotenv()

rootTag = SwaggerTag(name="Root", description="Root API operations")
healthCheckTag = SwaggerTag(name="HealthCheck", description="HealthCheck API operations")
qrcodeTag = SwaggerTag(name="QRCode", description="QRCode API operations")

description = """
Awesome FAST APIs at your service 🚀
"""

app = FastAPI(lifespan=lifespan, 
              title="Fast API Backend", 
              description=description, 
              summary="Fast API backend service v0.0.1",
              version="0.0.1",
              terms_of_service="https://github.com/aravinve/fastapi-backend/blob/main/LICENSE",
              contact={
                  "name": "Aravind Venkatesan",
                  "url": "https://aravinve.github.io"
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0"
              },
              openapi_url="/api/v1/openapi.json",
              swagger_ui_parameters={"docExpansion":"none"},
              openapi_tags=[
                  Tag(name=rootTag.name, description=rootTag.description),
                  Tag(name=healthCheckTag.name, description=healthCheckTag.description),
                  Tag(name=qrcodeTag.name, description=qrcodeTag.description),
                ]
            )

# Configure CORS Middleware

origins =[
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Configure Static Directory

app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Routers

app.include_router(qrcode.router, prefix="/api/v1/qrcode", tags=[qrcodeTag.name])

@app.get("/", response_class=JSONResponse, tags=[rootTag.name])
def root():
    return {
        "serviceName": "FastApi Python Service", 
        "message": "Welcome to the Fast API Backend",
        "author": "Aravind Venkatesan",
        "repository": "https://github.com/aravinve/fastapi-backend",
        "homepage": "/static/index.html"
    }

@app.get("/health", response_class=JSONResponse, tags=[healthCheckTag.name])
def check_health():
    return {"status": "OK"}

@app.get("/readiness", response_class=JSONResponse, tags=[healthCheckTag.name])
def check_readiness():
    # Add your custom readiness checks here
    # For example, check if your application dependencies are available
    # If everything is ready, return {"status": "OK"}
    return {"status": "OK"}

@app.get("/up", response_class=JSONResponse, tags=[healthCheckTag.name])
def get_server_uptime():
    server_uptime = datetime.now() - server_start_time
    return {"status": "OK", "uptime": str(server_uptime)}

if __name__ == "__main__":
    host = os.getenv("FASTAPI_HOST", "0.0.0.0")
    port = int(os.getenv("FASTAPI_PORT", 8000))
    print(f"Server using host={host}; port={port};")
    import uvicorn
    uvicorn.run(app, host, port)
