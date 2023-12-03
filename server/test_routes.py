from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import response_models

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

@router.api_route("/get_card", methods=['GET'], responses=
    {
        400: {"model": response_models.Response400},
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=FileResponse
)
async def get_card(params: str):
    if params == None or params == "":
        raise HTTPException(status_code=400, detail="Empty request")
    return FileResponse("test_image.png")
