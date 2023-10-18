from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.done as done_schema
import api.cruds.done as done_crud
from api.db import get_db

router = APIRouter()


@router.put("/tasks/{task_id}/waiting", response_model=done_schema.waitingResponse)
async def mark_task_as_waiting(task_id: int, db: AsyncSession = Depends(get_db)):
    waiting = await done_crud.get_waiting(db, task_id=task_id)
    if waiting is not None:
        raise HTTPException(status_code=400, detail="Waiting already exists")
    
    await done_crud.create_waiting(db, task_id)
    
    working = await done_crud.get_working(db, task_id=task_id)
    if working is not None:
        await done_crud.delete_working(db, original=working)

    done = await done_crud.get_done(db, task_id=task_id)
    if done is not None:
        await done_crud.delete_done(db, original=done)
    
    return {"message": "Task marked as waiting"}

@router.delete("/tasks/{task_id}/waiting", response_model=None)
async def unmark_task_as_waiting(task_id: int, db: AsyncSession = Depends(get_db)):
    waiting = await done_crud.get_waiting(db, task_id=task_id)
    if waiting is None:
        raise HTTPException(status_code=404, detail="Waiting not found")

    return await done_crud.delete_waiting(db, original=waiting)

@router.put("/tasks/{task_id}/working", response_model=done_schema.workingResponse)
async def mark_task_as_working(task_id: int, db: AsyncSession = Depends(get_db)):
    working = await done_crud.get_working(db, task_id=task_id)
    if working is not None:
        raise HTTPException(status_code=400, detail="Working already exists")
    
    await done_crud.create_working(db, task_id)
    
    waiting = await done_crud.get_waiting(db, task_id=task_id)
    if waiting is not None:
        await done_crud.delete_waiting(db, original=waiting)
    
    done = await done_crud.get_done(db, task_id=task_id)
    if done is not None:
        await done_crud.delete_done(db, original=done)
    
    return {"message": "Task marked as working"}


@router.delete("/tasks/{task_id}/working", response_model=None)
async def unmark_task_as_working(task_id: int, db: AsyncSession = Depends(get_db)):
    working = await done_crud.get_working(db, task_id=task_id)
    if working is None:
        raise HTTPException(status_code=404, detail="Working not found")
    
    return await done_crud.delete_working(db, original=working)

@router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=400, detail="Done already exists")
    
    await done_crud.create_done(db, task_id)

    waiting = await done_crud.get_waiting(db, task_id=task_id)
    if waiting is not None:
        await done_crud.delete_waiting(db, original=waiting)

    working = await done_crud.get_working(db, task_id=task_id)
    if working is not None:
        await done_crud.delete_working(db, original=working)

    return {"message": "Task marked as done"}



@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Done not found")

    return await done_crud.delete_done(db, original=done)