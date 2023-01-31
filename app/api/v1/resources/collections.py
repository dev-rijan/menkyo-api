from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repository.collection_repository import CollectionRepository
from app.api import deps

router = APIRouter()

# @router.get("/", response_model=List[schemas.Item])


@router.get("/")
def index(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve collections.
    """
    collections = CollectionRepository.get_all(db=db)
    print(collections)
    return collections
