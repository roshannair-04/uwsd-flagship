from sqlalchemy.orm import Session
from . import models, schemas

# Create
def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.person.Person(
        name=person.name,
        category=person.category
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# Read all
def get_people(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.person.Person).offset(skip).limit(limit).all()

# Read one
def get_person(db: Session, person_id: int):
    return db.query(models.person.Person).filter(models.person.Person.id == person_id).first()

# Update
def update_person(db: Session, person_id: int, updates: schemas.PersonUpdate):
    db_person = get_person(db, person_id)
    if not db_person:
        return None
    if updates.name is not None:
        db_person.name = updates.name
    if updates.category is not None:
        db_person.category = updates.category
    db.commit()
    db.refresh(db_person)
    return db_person

# Delete
def delete_person(db: Session, person_id: int):
    db_person = get_person(db, person_id)
    if not db_person:
        return None
    db.delete(db_person)
    db.commit()
    return db_person
