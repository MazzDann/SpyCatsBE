from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud_operationieles, schems, db_conf as TheDB

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000", # This is the origin you want to allow
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Allows all headers
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

def get_db():
    db = TheDB.SessionLocal()
    try:yield db
    finally:db.close()

# Cats
@app.post("/cats/", response_model=schems.Cat)
def create_cat(cat: schems.CatCreate, db: Session = Depends(get_db)):
    return crud_operationieles.create_cat(db, cat)

@app.get("/cats/", response_model=list[schems.Cat])
def list_cats(db: Session = Depends(get_db)):
    print(crud_operationieles.get_cats(db))
    return crud_operationieles.get_cats(db)

@app.get("/cats/{cat_id}", response_model=schems.Cat)
def get_cat(cat_id: int, db: Session = Depends(get_db)):
    return crud_operationieles.get_cat(db, cat_id)

@app.put("/cats/{cat_id}/salary", response_model=schems.Cat)
def update_cat_salary(cat_id: int, salary_update: schems.CatSalaryUpdate, db: Session = Depends(get_db)):
    return crud_operationieles.update_cat_salary(db, cat_id, salary_update.salary)

@app.delete("/cats/{cat_id}")
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    crud_operationieles.delete_cat(db, cat_id)
    return {"message": "Cat deleted"}

# Missions
@app.post("/missions/", response_model=schems.Mission)
def create_mission(mission: schems.MissionCreate, db: Session = Depends(get_db)):
    return crud_operationieles.create_mission(db, mission)

@app.get("/missions/", response_model=list[schems.Mission])
def list_missions(db: Session = Depends(get_db)):
    return crud_operationieles.get_missions(db)

@app.get("/missions/{mission_id}", response_model=schems.Mission)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    return crud_operationieles.get_mission(db, mission_id)

@app.delete("/missions/{mission_id}")
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    crud_operationieles.delete_mission(db, mission_id)
    return {"message": "Mission deleted"}

@app.put("/missions/{mission_id}/assign_cat", response_model=schems.Mission)
def assign_cat_to_mission(mission_id: int, cat_id: int, db: Session = Depends(get_db)):
    return crud_operationieles.assign_cat_to_mission(db, mission_id, cat_id)

@app.put("/targets/{target_id}/notes", response_model=schems.Target)
def update_target_notes(target_id: int, notes: str, db: Session = Depends(get_db)):
    return crud_operationieles.update_target_notes(db, target_id, notes)

@app.put("/targets/{target_id}/complete", response_model=schems.Target)
def mark_target_complete(target_id: int, db: Session = Depends(get_db)):
    return crud_operationieles.mark_target_complete(db, target_id)