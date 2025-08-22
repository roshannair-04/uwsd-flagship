from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import database, schemas, crud

app = FastAPI(title="UWSD - RoshTek Industries")


# Dependency: provide DB session for endpoints
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---- PERSON ENDPOINTS ---- #

@app.post("/person/", response_model=schemas.PersonOut)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db, person)


@app.get("/person/{person_id}", response_model=schemas.PersonOut)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@app.get("/people/", response_model=list[schemas.PersonOut])
def read_people(db: Session = Depends(get_db)):
    return crud.get_people(db)


@app.put("/person/{person_id}", response_model=schemas.PersonOut)
def update_person(person_id: int, person: schemas.PersonUpdate, db: Session = Depends(get_db)):
    updated_person = crud.update_person(db, person_id, person)
    if not updated_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return updated_person


@app.delete("/person/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_person(db, person_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"ok": True}
