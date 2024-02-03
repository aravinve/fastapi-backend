from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse
from datetime import datetime

from src.services.converters.json_yaml_converter import json_to_yaml_from_file, yaml_to_json_from_file

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

