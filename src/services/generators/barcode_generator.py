import io
from barcode import EAN13
from barcode.writer import ImageWriter
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

async def generate_barcode(request_data) -> StreamingResponse:
    try:
        barcode_data = str(request_data.data)
        barcode = EAN13(barcode_data, writer=ImageWriter())
        image_bytes = io.BytesIO()
        barcode.write(image_bytes)
        image_bytes.seek(0)
        return StreamingResponse(status_code=200, content=image_bytes, media_type="image/png")
    except Exception as e:
        error_message = {"error": str(e)}
        raise HTTPException(status_code=400, detail=jsonable_encoder(error_message))