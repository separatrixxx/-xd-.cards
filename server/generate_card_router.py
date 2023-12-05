from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
import request_models
import response_models
from pynter.pynter import generate_captioned
from io import BytesIO
import base64
import requests
import json

router = APIRouter(
    prefix="/imageGeneration",
    tags=["imageGeneration"]
)

stable_diffusion_url = "https://api.wizmodel.com/sdapi/v1/txt2img"

api_key = open('stable_diffusion_token.txt').read()

font_path = "./font.ttf"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

    
def get_stable_diffusion_image(text: str):
    payload = json.dumps({
        "prompt": text,
        "steps": 50
    })
    response = requests.request("POST", stable_diffusion_url, headers=headers, data=payload)
    base64_string = response.json()['images'][0]
    image_data = base64.b64decode(base64_string)
    image_bytes = BytesIO(image_data)
    return image_bytes


@router.post("/generateCard", responses=
    {
        400: {"model": response_models.Response400},
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response
)
async def generate_card(params_for_image: request_models.QueryParams):
    if params_for_image.text_stable_diffusion == None or params_for_image.text_stable_diffusion == "":
        raise HTTPException(status_code=400, detail="No text for Stable Diffusion text was defined")
    image_bytes = get_stable_diffusion_image(params_for_image.text_stable_diffusion)
    if (b'loading' not in image_bytes.getvalue()):
        if (params_for_image.text_image != None and params_for_image.text_image != ""):
            im = generate_captioned(params_for_image.text_image, image_path=image_bytes, size=(512, 512),
                                font_path=font_path, filter_color=(0, 0, 0, 20))
            image_bytes_result = BytesIO()
            im.convert("RGB").save(image_bytes_result, format='PNG')
            image_bytes = image_bytes_result
        return Response(content=image_bytes.getvalue(), media_type="image/png")
    raise HTTPException(status_code=400, detail="Stable Diffusion needs some time (around 10-13 minutes) to cool down")
