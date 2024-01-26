import io
import tempfile
import segno

from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from src.models.generator_models import QRCodeGeneratorRequest, DataTypeEnum

async def generate_qrcode(http_client, request_data: QRCodeGeneratorRequest) -> StreamingResponse:
    validate_url(request_data.data, request_data.data_type)
    try:
        qr = segno.make_qr(request_data.data)
        size = request_data.size.numeric_value
        background_image_url = request_data.background_image_url
        color = request_data.color
        if background_image_url is not None:
            return await generate_qrcode_with_background(http_client, qr, size, background_image_url, color)
        else:
            return generate_qrcode_default(qr, size, color)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Please contact the API admin. Unable to generate QRCode! Reason={e}")
    
def validate_url(data: str, data_type: DataTypeEnum):
    if data_type == DataTypeEnum.url and not (data.startswith("http://") or data.startswith("https://")):
        raise HTTPException(status_code=400, detail="data must be a valid URL when data_type=url")

async def generate_qrcode_with_background(http_client, qr, size: int, background_image_url: str, color: str) -> StreamingResponse:
    image_content = await http_client.download_image(background_image_url)
    file_extension = determine_image_extension(http_client, image_content)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
        temp_file.write(image_content)
        apply_artistic_effect(qr, size, temp_file.name, color)
        
        with open(temp_file.name, "rb") as file_content:
            final_content = io.BytesIO(file_content.read())
            return StreamingResponse(status_code=200, content=final_content, media_type=f"image/{file_extension[1:]}")

def generate_qrcode_default(qr, size: int, color: str) -> StreamingResponse:
    default_file_extension = ".png"
    with tempfile.NamedTemporaryFile(delete=False, suffix=default_file_extension) as temp_file:
        qr.save(temp_file.name, scale=size, border=2, dark=color)
        
        with open(temp_file.name, "rb") as file_content:
            final_content = io.BytesIO(file_content.read())
            temp_file.close()
            return StreamingResponse(status_code=200, content=final_content, media_type=f"image/{default_file_extension[1:]}")

def determine_image_extension(http_client, image_content: bytes) -> str:
    image_type = http_client.guess_image_type(image_content)
    if image_type in {"gif", "png", "jpeg", "jpg"}:
        return f".{image_type}"
    raise HTTPException(status_code=400, detail="Unsupported image format")

def apply_artistic_effect(qr, size: int, background_path: str, color: str):
    qr.to_artistic(background=background_path, target=background_path, scale=size, border=2, dark=color)