from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
import model.request_models as request_models
import model.response_models as response_models
import service.generate_card_service 

generate_card_service = service.generate_card_service.GenerateCardService()

router = APIRouter(
    prefix="/imageGeneration",
    tags=["imageGeneration"]
)


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
    try:
        image_bytes = generate_card_service.generate_card(params_for_image)
        return Response(content=image_bytes.getvalue(), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
