from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    waiting = relationship("Waiting", back_populates="task", cascade="delete")
    working = relationship("Working", back_populates="task", cascade="delete")
    done = relationship("Done", back_populates="task", cascade="delete")


class Waiting(Base):
    __tablename__ = "waiting"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="waiting")

class Working(Base):
    __tablename__ = "working"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="working")

class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="done")