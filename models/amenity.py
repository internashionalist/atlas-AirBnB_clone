#!/usr/bin/python3
"""
Amenity class module for AirBnB clone
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines attributes and methods for Amenity class

    Attributes:
        name (str):  name of amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to initialize instance

        Attributes:
            name (str): name of amenity

        Returns:
            None
        """
        super().__init__(*args, **kwargs)  # call inherited __init__ method
        self.name = ""  # initialize name attribute
        if kwargs:
            for key, value in kwargs.items():  # assign key-value pairs to attributes
                if key == 'name':  # if key is the name
                    self.name = kwargs.get('name')  # assign value to name attribute
