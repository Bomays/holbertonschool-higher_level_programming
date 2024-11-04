#!/usr/bin/python3
"""
    Module that use with SQLAlchemy's ORM
    to facilitate interactions of the class with cities
    table in dedicated database, allowing CRUD
    actions on state records
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    Class that represents a city in the cities table
    of hbtn_0e_14_usa database

    Attributes:
        id (int): Unique id for the sate, autogenerated
                and set as primary key, cannot be NUll
        name (str): name of the city, cannot be NULL
        state_id (int): name of the state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")