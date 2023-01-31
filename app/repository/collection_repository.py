from app.repository.base import BaseRepository
from app.models.collection import Collection


class CollectionRepository(BaseRepository[Collection]):
    pass


collection = CollectionRepository(Collection)
