from fastapi import FastAPI

app = FastAPI(title="UWSD - RoshTek Industries")

@app.get("/")
def read_root():
    return {"message": "Welcome to UWSD - RoshTek Industries API"}
