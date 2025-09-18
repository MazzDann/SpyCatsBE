from pydantic import BaseModel, field_validator
from typing import List, Optional

from src.ext_api import validate_breed

class CatBase(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: float

class CatCreate(CatBase):
    @field_validator("breed")
    def validate_breed(cls, value):
        return validate_breed(value)

class Cat(CatBase):
    id: int
    class Config:
        orm_mode = True

class TargetBase(BaseModel):
    name: str
    country: str
    notes: Optional[str] = ""
    complete: bool = False

class MissionBase(BaseModel):
    cat_id: Optional[int] = None
    complete: bool = False
    targets: List[TargetBase]

class MissionCreate(MissionBase):
    targets: List[TargetBase]
    @field_validator("targets")
    # validator is quite old(
    def validate_targets(cls, value):
        if not (1 <= len(value) <= 3):
            raise ValueError("Mission must have 1 to 3 targets, srry")
        return value

class Mission(MissionBase):
    id: int
    class Config:
        orm_mode = True

class Target(TargetBase):
    id: int
    mission_id: int
    class Config:
        orm_mode = True