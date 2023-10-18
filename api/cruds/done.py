from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model


async def get_waiting(db: AsyncSession, task_id: int) -> Optional[task_model.Waiting]:
    result: Result = await db.execute(
        select(task_model.Waiting).filter(task_model.Waiting.id == task_id)
    )
    waiting: Optional[Tuple[task_model.Waiting]] = result.first()
    return waiting[0] if waiting is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def create_waiting(db: AsyncSession, task_id: int) -> task_model.Waiting:
    waiting = task_model.Waiting(id=task_id)
    db.add(waiting)
    await db.commit()
    await db.refresh(waiting)
    return waiting


async def delete_waiting(db: AsyncSession, original: task_model.Waiting) -> None:
    await db.delete(original)
    await db.commit()

##

async def get_working(db: AsyncSession, task_id: int) -> Optional[task_model.Working]:
    result: Result = await db.execute(
        select(task_model.Working).filter(task_model.Working.id == task_id)
    )
    working: Optional[Tuple[task_model.Working]] = result.first()
    return working[0] if working is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def create_working(db: AsyncSession, task_id: int) -> task_model.Working:
    working = task_model.Working(id=task_id)
    db.add(working)
    await db.commit()
    await db.refresh(working)
    return working


async def delete_working(db: AsyncSession, original: task_model.Working) -> None:
    await db.delete(original)
    await db.commit()

##

async def get_done(db: AsyncSession, task_id: int) -> Optional[task_model.Done]:
    result: Result = await db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    done: Optional[Tuple[task_model.Done]] = result.first()
    return done[0] if done is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
    done = task_model.Done(id=task_id)
    db.add(done)
    await db.commit()
    await db.refresh(done)
    return done


async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
    await db.delete(original)
    await db.commit()