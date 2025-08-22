from pydantic import BaseModel
from .models.person import PersonCategory


# Shared properties
class PersonBase(BaseModel):
    name: str
    category: PersonCategory


# Schema for creating a new person
class PersonCreate(PersonBase):
    pass


# Schema for updating an existing person
class PersonUpdate(BaseModel):
    name: str | None = None
    category: PersonCategory | None = None


# Schema for sending data back to client
class PersonOut(PersonBase):
    id: int

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2
