from sqlalchemy.orm import Session, joinedload
from app.repository.base import BaseRepository
from app.models.collection import Collection


class CollectionRepository(BaseRepository[Collection]):
    def get_by_slug(
        self,
        slug: str,
        db: Session
    ) -> Collection:
        return db.query(self.model)\
            .options(joinedload(self.model.questions))\
            .where(Collection.slug == slug)\
            .first()


collection = CollectionRepository(Collection)
