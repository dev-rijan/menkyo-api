from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repository.collection_repository import collection
from app.api import deps
from app.schemas.collection import Collection as CollectionSchema

router = APIRouter()


@router.get("/", response_model=List[CollectionSchema])
def index(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve collections.
    """
    collections = collection.get_all(db=db, skip=skip, limit=limit)
    return collections
