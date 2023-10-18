from pydantic import BaseModel


class DoneResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True

class waitingResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True

class workingResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True