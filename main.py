from fastapi import FastAPI, Request
import base64
import requests

app = FastAPI()

@app.post("/to_base64")
async def to_base64(request: Request):
    data = await request.json()
    image_url = data.get("image_url")
    if not image_url:
        return {"error": "No image_url provided"}

    try:
        response = requests.get(image_url)
        response.raise_for_status()
        base64_str = base64.b64encode(response.content).decode('utf-8')
        return {"base64_image": base64_str}
    except Exception as e:
        return {"error": str(e)}
