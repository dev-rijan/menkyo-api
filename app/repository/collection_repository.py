from sqlalchemy.orm import Session
from app.repository.base import BaseRepository
from app.models.collection import Collection


class CollectionRepository(BaseRepository[Collection]):
    def get_by_slug(
        self, slug: str,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100
    ) -> Collection:
        return db.query(self.model).filter(Collection.slug == slug).one()


collection = CollectionRepository(Collection)
