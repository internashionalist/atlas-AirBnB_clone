#!/usr/bin/python3
"""
City class module for AirBnB clone
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Beginning stage of City class

    Attributes:
        state_id (str):  state id
        name (str):      city name
    """
    state_id = ""
    name = ""
