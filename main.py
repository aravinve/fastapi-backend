from fastapi import FastAPI
from src.routes import qrcode

app = FastAPI()

app.include_router(qrcode.router, prefix="/qrcode", tags=["qrcode"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the QR Code Generator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
