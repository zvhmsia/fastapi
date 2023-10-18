from typing import Optional

from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

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