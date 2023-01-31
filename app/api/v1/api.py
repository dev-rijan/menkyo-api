from fastapi import APIRouter
from app.api.v1.resources import collections

api_router = APIRouter()
api_router.include_router(
    collections.router,  prefix="/collections", tags=["collections"]
)
