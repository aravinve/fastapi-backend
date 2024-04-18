import requests

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from src.utils.external_apis import zen_quotes_api_url

async def generate_quote():
    response = requests.get(zen_quotes_api_url)
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        result = f'{quote} - {author}'
        return result
    else:
        error_message = {"error": "Failed to fetch"}
        raise HTTPException(status_code=response.status_code, detail=jsonable_encoder(error_message))
