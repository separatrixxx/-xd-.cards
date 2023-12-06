from pydantic import BaseModel

class QueryParams(BaseModel):
    text_stable_diffusion: str | None = None
    text_image: str | None = None