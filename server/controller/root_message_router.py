from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(
    prefix = "")

@router.get("/", responses=
    {
        200: {
            "content": {"application/json": {}}
        }
    }
)
async def root_message():
    return {"xd.cards": "by muff team"}
