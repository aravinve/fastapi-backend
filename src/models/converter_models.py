from pydantic import BaseModel

class JsonToYamlRequest(BaseModel):
    json_content: str

class YamlToJsonRequest(BaseModel):
    yaml_content: str