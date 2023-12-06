import service.stable_diffusion_service
import model.request_models as request_models
from pynter.pynter import generate_captioned
from io import BytesIO

class GenerateCardService:
    
    def __init__(self):
        self.__stable_diffusion_service = service.stable_diffusion_service.StableDiffusionService()
        self.__font_path = "./service/font.ttf"

    def generate_card(self, params_for_image : request_models.QueryParams):
        if params_for_image.text_stable_diffusion == None or params_for_image.text_stable_diffusion == "":
            raise ValueError("No text for Stable Diffusion text was defined")
        image_bytes = ""
        try:
            image_bytes = self.__stable_diffusion_service.get_stable_diffusion_image(params_for_image.text_stable_diffusion)
        except Exception as e:
            raise ValueError(e)
        if (params_for_image.text_image != None and params_for_image.text_image != ""):
            im = generate_captioned(params_for_image.text_image, image_path=image_bytes, size=(512, 512),
                                font_path=self.__font_path, filter_color=(0, 0, 0, 20))
            image_bytes_result = BytesIO()
            im.convert("RGB").save(image_bytes_result, format='PNG')
            image_bytes = image_bytes_result
        return image_bytes