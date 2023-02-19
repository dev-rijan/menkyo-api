from typing import List
from pydantic import BaseModel


class Collection(BaseModel):
    slug: str
    description: str

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: int
    title: str
    description: str
    answer: bool

    class Config:
        orm_mode = True


class CollectionQuestion(Collection):
    questions: List[Question]
