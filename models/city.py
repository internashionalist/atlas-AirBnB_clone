#!/usr/bin/python3
"""
City class module for AirBnB clone
"""

from models.base_model import BaseModel
from datetime import datetime


class City(BaseModel):
    """
    Beginning stage of City class

    Attributes:
        state_id (str):  state id
        name (str):      city name
    """
    state_id = ""
    name = ""

    def __init__(self, **kwargs):
        if not kwargs:
            super().__init__()
        else:
            for key, value in kwargs.items():
                if key == 'created_at':
                    created_text = kwargs.get('created_at')
                    formated_text = datetime.strptime(
                        created_text, '%Y-%m-%dT%H:%M:%S.%f')
                    self.created_at = formated_text
                elif key == 'updated_at':
                    updated_text = kwargs.get('updated_at')
                    formated_text = datetime.strptime(
                        updated_text, '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = formated_text
                elif key != '__class__':
                    setattr(self, key, value)
