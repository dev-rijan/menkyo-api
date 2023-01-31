from fastapi import FastAPI
from app.settings import settings
from app.api.v1.api import api_router


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    app.include_router(api_router)

    return app
