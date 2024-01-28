from enum import Enum
from typing import Optional
from pydantic import BaseModel, HttpUrl, validator
import sys


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

class NumberGeneratorRequest(BaseModel):
    count: int = 1
    min: int = -sys.maxsize - 1
    max: int = sys.maxsize

class BarcodeGeneratorRequest(BaseModel):
    data: int
    
    @validator("data")
    def validate_data_length(cls, value):
        min_length = 12
        str_value = str(value)
        if len(str_value) < min_length:
            raise ValueError(f"Value must be an integer with a minimum length of {min_length} digits.")
        return value
    
class FakerCategory(str, Enum):
    username = "username"
    address = "address"
    firstname = "firstname"
    lastname = "lastname"
    email = "email"
    phone_number = "phone_number"
    date_of_birth = "date_of_birth"
    company = "company"
    word = "word"
    sentence = "sentence"
    paragraph = "paragraph"
    text = "text"
    emoji = "emoji"
    date = "date"
    profile = "profile"
    location = "location"
    currency = "currency"

class FakerGeneratorRequest(BaseModel):
    count: int = 1
    fakerCategory: Optional[FakerCategory] = FakerCategory.username

    @validator("count")
    def validate_data_length(cls, value):
        max_length = 100
        if value > max_length:
            raise ValueError(f"Value cannot be greater than {max_length}.")
        return value