#!/usr/bin/python3
"""Module that defines the State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Represent a state."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
