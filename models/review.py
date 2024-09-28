#!/usr/bin/python3
"""
Review class module for AirBnB clone
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Beginning stage of Review class

    Attributes:
        place_id (str):   place id
        user_id (str):    user id
        text (str):       review text
    """
    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
