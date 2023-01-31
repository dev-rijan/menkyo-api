
from sqlalchemy import Column, Integer, String, Boolean

from app.models.base import Base


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    answer = Column(Boolean, nullable=False)
