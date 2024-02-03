from pdf2image import convert_from_bytes
import tempfile
import zipfile
import os
import io
from fastapi.responses import StreamingResponse

"""
PDF to Image
    - Single page pdf means single image
    - Multiple page pdf means multiple images
"""

def pdf_to_image_from_file(pdf_content: bytes, zip_filename: str) -> bytes:
    output_image_format = "png"
    images = convert_from_bytes(pdf_content, fmt=output_image_format, poppler_path=r"D:\workspace\fastapi-backend\libraries\poppler-23.11.0\Library\bin")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_zip:
        with zipfile.ZipFile(temp_zip.name, 'w') as zip_file:
            for i, image in enumerate(images):
                image_path = f"image_{i + 1}.png"
                image.save(image_path, "PNG")
                zip_file.write(image_path, os.path.basename(image_path))

    # Send the zip file as a response
    with open(temp_zip.name, 'rb') as zip_file:
        content = zip_file.read()
        return StreamingResponse(content=io.BytesIO(content), media_type="application/zip", headers={"Content-Disposition": f"attachment; filename={zip_filename}"})