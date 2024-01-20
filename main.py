from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import segno

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the QR Code Generator API"}

# @app.get("/generate_qrcode/{data}")
# def generate_qrcode(data: str):
#     # Generate QR code using segno
#     qr = segno.make(data)

#     # Save the QR code as a PNG image in memory
#     image = qr.png(encode=True)

#     # Return the image as a streaming response
#     return StreamingResponse(content=image, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
