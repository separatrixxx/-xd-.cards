from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import response_models
from pynter.pynter import generate_captioned

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
    im = generate_captioned(params, image_path="./test_image.png", size=(512, 512),
                        font_path="./font.ttf", filter_color=(0, 0, 0, 20))
    im.convert("RGB").save("new_test_image.png")
    return FileResponse("new_test_image.png")
