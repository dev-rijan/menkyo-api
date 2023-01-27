
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base

class Collection(Base):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(SmallInteger, index=True, nullable=False)
    slug = Column(String, index=True, nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)