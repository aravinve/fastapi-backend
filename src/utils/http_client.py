import httpx
import imghdr
from pydantic import HttpUrl

class DownloadClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def download_image(self, url: HttpUrl) -> bytes:
        response = await self.client.get(str(url))
        response.raise_for_status()
        return response.content
    
    def guess_image_type(self, content: bytes) -> str:
        return imghdr.what(None, content)

    async def close(self):
        await self.client.aclose()
