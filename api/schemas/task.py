from typing import Optional
from datetime import date

from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    start_date: Optional[date] = Field(default_factory=date.today)
    start_schedule_date: Optional[date] = Field(default_factory=date.today)
    fin_date: Optional[date] = Field(default_factory=date.today)
    fin_schedule_date: Optional[date] = Field(default_factory=date.today)
    user_name: Optional[str] = Field(None, example="廣石健悟")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    waiting: bool = Field(False, description="未着手")
    working: bool = Field(False, description="着手中")
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True