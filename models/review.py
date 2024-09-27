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
    place_id = ""
    user_id = ""
    text = ""
