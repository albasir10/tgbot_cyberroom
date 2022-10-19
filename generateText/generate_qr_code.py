import requests


async def create_qr_code(code: str):
    response = requests.get("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + code)
    return response.content
