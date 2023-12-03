from pydantic import BaseModel

class ResponseDetail(BaseModel):
    detail: str

class Response200(ResponseDetail):
    pass

class Response400(ResponseDetail):
    pass
