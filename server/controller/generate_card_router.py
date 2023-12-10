from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
import model.request_models as request_models
import model.response_models as response_models
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import service.generate_card_service 

generate_card_service = service.generate_card_service.GenerateCardService()

router = APIRouter(
    prefix="/imageGeneration",
    tags=["imageGeneration"]
)


@router.post("/generateCard")
async def generate_card(params_for_image: request_models.QueryParams):
    try:
        image_bytes = generate_card_service.generate_card(params_for_image)
        json_compatible_data = jsonable_encoder(response_models.Response200(detail = str(image_bytes)))
        return JSONResponse(content=json_compatible_data)
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))
