from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from src.models.generator_models import  QRCodeGeneratorRequest, UUIDGeneratorRequest, TextGeneratorRequest, SecretGeneratorRequest, ColorGeneratorRequest, NumberGeneratorRequest, BarcodeGeneratorRequest, FakerGeneratorRequest, FakerCategory

from src.services.generators.qrcode_generator import generate_qrcode
from src.services.generators.uuid_generator import generate_random_uuids
from src.services.generators.text_generator import generate_random_text
from src.services.generators.secret_generator import generate_random_secure_text
from src.services.generators.color_generator import generate_random_hex_color
from src.services.generators.number_generator import generate_random_numbers
from src.services.generators.barcode_generator import generate_barcode
from src.services.generators.faker_generator import generate_random

from src.utils.http_client import DownloadClient

router = APIRouter()
http_client = DownloadClient()


@router.post("/qrcode")
async def qrcode_generator(request_data: QRCodeGeneratorRequest) -> StreamingResponse:
    return await generate_qrcode(http_client, request_data)

@router.post("/uuid")
def uuid_generator(request_data: UUIDGeneratorRequest) -> dict:
    result = generate_random_uuids(request_data.count, request_data.hyphens, request_data.uppercase)
    count = len(result)
    return {"result": result, "count": count}

@router.post("/text")
def text_generator(request_data: TextGeneratorRequest) -> dict:
    result = generate_random_text(request_data.count, request_data.length, request_data.letters, request_data.digits, request_data.punctuation, request_data.whitespace)
    count = len(result)
    return {"result": result, "count": count}

@router.post("/secret")
def secret_generator(request_data: SecretGeneratorRequest) -> dict:
    result = generate_random_secure_text(request_data.count, request_data.length)
    count = len(result)
    return {"result": result, "count": count}

@router.post("/color")
def color_generator(request_data: ColorGeneratorRequest) -> dict:
    result = generate_random_hex_color(request_data.count)
    count = len(result)
    return {"result": result, "count": count}

@router.post("/number")
def number_generator(request_data: NumberGeneratorRequest) -> dict:
    result = generate_random_numbers(request_data.count, request_data.min, request_data.max)
    count = len(result)
    return {"result": result, "count": count}

@router.post("/barcode")
async def barcode_generator(request_data: BarcodeGeneratorRequest) -> StreamingResponse:
    return await generate_barcode(request_data)

@router.post("/faker")
def faker_generator(request_data: FakerGeneratorRequest) -> dict:
    result = generate_random(request_data.fakerCategory, request_data.count)
    count = len(result)
    return {"result": result, "count": count}