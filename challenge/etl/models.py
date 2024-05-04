from enum import Enum as PythonEnum
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, Enum, Float, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class ValidCakeFlavors(PythonEnum):
    BUTTER = "butter"
    CARROT = "carrot"
    BLACK_FOREST = "black forest"
    AVOCADO = "avocado"
    VANILLA = "vanilla"
    CARAMEL = "caramel"
    RAINBOW = "rainbow"
    CHIFFON = "chiffon"
    CREAM = "cream"
    BABKA = "babka"
    SPONGE = "sponge"
    APPLE = "apple"
    STRAWBERRY = "strawberry"
    BISCUIT = "biscuit"
    CHOCOLATE = "chocolate"


VALID_UNITS = ["mm", "in", "m"]


class CakeSqlalchemyOrm(Base):
    """
    sqlalchemy model of Cake document
    """

    __tablename__ = "cakes"

    entry_id = Column(Integer, primary_key=True)
    name = Column(Enum(ValidCakeFlavors), String(20))
    diameter_in_mm = Column(Float, nullable=False)
    vegan = Column(Boolean, nullable=True)
    cake_entry_timestamp = Column(DateTime, nullable=False)


class CakeModel(BaseModel):
    """
    Pydantic model of a cake for data validation
    """

    entry_id: int = Field(description="The entry id of the cake")
    name: Optional[str] = Field(description="Name (or type) of the cake", default=None)
    diameter_in_mm: float = Field(description="Diameter of the cake in millimeters")
    vegan: Optional[bool] = Field(
        description="Specifies if cake is vegan or not", default=None
    )
    cake_entry_timestamp: datetime


def create_tables(connection_url: str):
    """
    Creates the DB tables corresponding to the ORM model.

    Args:
        connection_url: the URL to an SQL database.
    """
    engine = create_engine(connection_url, echo=True)
    Base.metadata.create_all(engine)
