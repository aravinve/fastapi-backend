from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from datetime import datetime

from src.services.converters.json_yaml_converter import json_to_yaml_from_file, yaml_to_json_from_file
from src.services.converters.image_to_pdf_converter import image_to_pdf_from_file
from src.services.converters.pdf_to_image_converter import pdf_to_image_from_file

router = APIRouter()

@router.post("/json-to-yaml")
async def json_to_yaml_converter_from_file(file: UploadFile = File(...)):
    json_content = await file.read()
    result = json_to_yaml_from_file(json_content)
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{file.filename.rsplit('.', 1)[0]}_{current_datetime}.yaml"
    return StreamingResponse(content=result, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})

@router.post("/yaml-to-json")
async def yaml_to_json_converter_from_file(file: UploadFile = File(...)):
    yaml_content = await file.read()
    result = yaml_to_json_from_file(yaml_content)
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{file.filename.rsplit('.', 1)[0]}_{current_datetime}.json"
    return StreamingResponse(content=result, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})


@router.post("/image-to-pdf")
async def image_to_pdf_converter_from_file(files: list[UploadFile] = File(...)):
    image_files = [await file.read() for file in files]
    result = image_to_pdf_from_file(image_files)
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"merged_images_{current_datetime}.pdf"
    return StreamingResponse(content=result, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})

@router.post("/pdf-to-image")
async def pdf_to_image_converter_from_file(file: UploadFile = File(...)):
    pdf_file = await file.read()
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    zip_filename = f"{file.filename.rsplit('.', 1)[0]}_{current_datetime}.zip"
    return pdf_to_image_from_file(pdf_file, zip_filename)
    