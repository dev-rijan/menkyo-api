from typing import Collection, Optional
from pydantic import BaseModel


class Collection(BaseModel):
    slug: str
    description: str

    class Config:
        orm_mode = True
