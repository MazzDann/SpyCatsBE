from sqlalchemy.orm import Session
# from . import models, schems
from fastapi import HTTPException

from .models import Cat, Mission, Target
from .schems import CatCreate, MissionCreate


# Cats :cat:
# emotes doesn't work T_T
def create_cat(db: Session, cat: CatCreate):
    db_cat = Cat(**cat.model_dump())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def get_cats(db: Session):return db.query(Cat).all()

def get_cat(db: Session, cat_id: int):
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:raise HTTPException(status_code=404, detail="Cat not found")
    return cat

def update_cat_salary(db: Session, cat_id: int, salary: float):
    cat = get_cat(db, cat_id)
    cat.salary = salary
    db.commit()
    db.refresh(cat)
    return cat

def delete_cat(db: Session, cat_id: int):
    cat = get_cat(db, cat_id)
    if cat.mission:raise HTTPException(status_code=400, detail="Cat is assigned to a mission")
    db.delete(cat)
    db.commit()

# Missions 
def create_mission(db: Session, mission: MissionCreate):
    db_mission = Mission(cat_id=mission.cat_id, complete=False)
    db.add(db_mission)
    db.commit()
    for target in mission.targets:
        db_target = Target(**target.model_dump(), mission_id=db_mission.id)
        db.add(db_target)
    db.commit()
    db.refresh(db_mission)
    return db_mission

def get_missions(db: Session):return db.query(Mission).all()

def get_mission(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:raise HTTPException(status_code=404, detail="Mission not found")
    return mission

def delete_mission(db: Session, mission_id: int):
    mission = get_mission(db, mission_id)
    if mission.cat_id:raise HTTPException(status_code=400, detail="Mission is assigned to a cat")
    db.delete(mission)
    db.commit()

def assign_cat_to_mission(db: Session, mission_id: int, cat_id: int):
    mission = get_mission(db, mission_id)
    cat = get_cat(db, cat_id)
    if cat.mission:raise HTTPException(status_code=400, detail="Cat already has a mission")
    mission.cat_id = cat_id
    db.commit()
    db.refresh(mission)
    return mission

def update_target_notes(db: Session, target_id: int, notes: str):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:raise HTTPException(status_code=404, detail="Target not found")
    if target.complete or target.mission.complete:
        raise HTTPException(status_code=400, detail="Cannot update notes: target or mission is complete")
    # too long
    target.notes = notes
    db.commit()
    db.refresh(target)
    return target

def mark_target_complete(db: Session, target_id: int):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:raise HTTPException(status_code=404, detail="Target not found")
    target.complete = True
    db.commit()
    # Check if all targets are complete, and spyed on
    # eheheheeh)
    mission = db.query(Mission).filter(Mission.id == target.mission_id).first()
    if all(t.complete for t in mission.targets):mission.complete = True
    db.commit()
    db.refresh(target)
    return target