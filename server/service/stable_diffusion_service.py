from io import BytesIO
import base64
import requests
import json

class StableDiffusionService:
    
    def __init__(self):
        self.__stable_diffusion_url = "https://api.wizmodel.com/sdapi/v1/txt2img"
        self.__api_key = ""
        try:
            self.__api_key = open('stable_diffusion_token.txt').read()
        except:
            raise ValueError("No token for Stable Diffusion was provided in stable_diffusion_token.txt file or file is missing or corrupted")
        if (self.__api_key == ""):
            raise ValueError("No token for Stable Diffusion was provided in stable_diffusion_token.txt")
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
        if (b'loading' in image_bytes.getvalue()):
            raise ValueError("Stable Diffusion needs some time (around 10-13 minutes) to cool down") 
        return image_bytes