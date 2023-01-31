from typing import List
from pydantic import BaseModel


class Collection(BaseModel):
    slug: str
    description: str

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: str
    title: str
    description: str
    answer: str

    class Config:
        orm_mode = True


class CollectionQuestion(Collection):
    questions: List[Question]
