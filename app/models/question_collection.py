
from sqlalchemy import Column, Integer, ForeignKey

from app.models.base import Base


class QuestionCollection(Base):
    __tablename__ = 'question_collections'

    question_id = Column(
        Integer,
        ForeignKey('questions.id'),
        index=True,
        primary_key=True
    )
    collection_id = Column(
        Integer,
        ForeignKey('collections.id'),
        index=True,
        primary_key=True
    )
