from pydantic import BaseModel

class SwaggerTag(BaseModel):
    name: str
    description: str