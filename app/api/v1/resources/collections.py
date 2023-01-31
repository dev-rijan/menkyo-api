from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.repository.collection_repository import collection
from app.api import deps
from app.schemas.collection import Collection as CollectionSchema, CollectionQuestion


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


@router.get("/{slug}", response_model=CollectionQuestion)
def get_by_slug(
    slug: str,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve collections.
    """
    collection_question = collection.get_by_slug(
        slug=slug,
        db=db
    )

    if not collection_question:
        raise HTTPException(
            status_code=404,
            detail="The collection with this slug does not exist in the system.",
        )

    return collection_question
