#!/usr/bin/python3
"""
User class module for AirBnB clone
"""
from models.base_model import BaseModel
from datetime import datetime



class User(BaseModel):
    """
    Beginning stage of User class

    Attributes:
        email (str):      user email
        password (str):   user password
        first_name (str): user first name
        last_name (str):  user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

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
