from io import BytesIO
import base64
import requests
import json

class StableDiffusionService:
    
    def __init__(self):
         self.__stable_diffusion_url = "https://api.wizmodel.com/sdapi/v1/txt2img"
         self.__api_key = open('stable_diffusion_token.txt').read()
         self.__headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.__api_key
            }
        
    def get_stable_diffusion_image(self, text: str):
        payload = json.dumps({
            "prompt": text,
            "steps": 50
        })
        response = requests.request("POST", self.__stable_diffusion_url, headers=self.__headers, data=payload)
        base64_string = response.json()['images'][0]
        image_data = base64.b64decode(base64_string)
        image_bytes = BytesIO(image_data)
        return image_bytes