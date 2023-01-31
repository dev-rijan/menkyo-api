
from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy.orm import relationship

from app.models.base import Base


class Collection(Base):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(SmallInteger, index=True, nullable=False)
    slug = Column(String, index=True, nullable=False)
    title = Column(String, nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)

    questions = relationship(
        "Question", secondary="question_collections", back_populates='collections')
