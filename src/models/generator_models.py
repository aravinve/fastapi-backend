from enum import Enum
from typing import Optional
from pydantic import BaseModel, HttpUrl


class DataTypeEnum(str, Enum):
    text = "text"
    url = "url"

class SizeEnum(str, Enum):
    small = "s", 2
    medium = "m", 5
    large = "l", 7
    extra_large = "xl", 10
    poster = "xxl", 20

    def __new__(cls, *args):
        obj = str.__new__(cls)
        obj._value_ = args[0]
        obj.numeric_value = args[1]
        return obj

class QRCodeGeneratorRequest(BaseModel):
    data: str
    data_type: DataTypeEnum
    background_image_url: Optional[HttpUrl] = None
    size: Optional[SizeEnum] = SizeEnum.medium
    color: str = '#000'

class UUIDGeneratorRequest(BaseModel):
    hyphens: bool = False
    uppercase: bool = False
    count: int = 1

class TextGeneratorRequest(BaseModel):
    count: int = 1
    length: int = 1
    letters: bool = True
    digits: bool = False
    punctuation: bool = False
    whitespace: bool = False

class SecretGeneratorRequest(BaseModel):
    count: int = 1
    length: int = 10

class ColorGeneratorRequest(BaseModel):
    count: int = 1