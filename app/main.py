from fastapi import FastAPI
from app.settings import settings


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    print(settings)

    return app
