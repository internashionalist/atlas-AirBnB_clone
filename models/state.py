#!/usr/bin/python3
"""
State class module for AirBnB clone
"""

from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):
    """
    Beginning stage of State class

    Attributes:
        name (str):  state name
    """
    def __init__(self, *args, **kwargs):
        if not kwargs:
            super().__init__()
            self.name = ""
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs.get('id')
                elif key == 'created_at':
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
