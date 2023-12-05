from fastapi import FastAPI
import generate_card_router as generate_card
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(generate_card.router)

origins = [
    "http://localhost"
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def test():
    return {"xd.cards": "by muff team"}

def custom_openapi():
	if app.openapi_schema:
		return app.openapi_schema
	openapi_schema = get_openapi(
    	title="[xd].cards",
		version="beta 0.1",
		description="API к сервису по созданию открыток \"[xd].cards\"\n\nby muff team",
		routes=app.routes,
	)
	app.openapi_schema = openapi_schema
	return app.openapi_schema

app.openapi = custom_openapi
