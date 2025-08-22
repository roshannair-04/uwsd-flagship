from sqlalchemy import Column, Integer, String, Enum
from ..database import Base
import enum

class PersonCategory(str, enum.Enum):
    SAFE = "Safe"
    THREAT = "Threat"
    WANTED = "Wanted"
    UNKNOWN = "Unknown"

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)   # UID
    name = Column(String, index=True)
    category = Column(Enum(PersonCategory), default=PersonCategory.UNKNOWN)
