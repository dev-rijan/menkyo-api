from fastapi import FastAPI
from app.settings import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    print(settings)

    return app
