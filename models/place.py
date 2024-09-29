#!/usr/bin/python3
"""
Place class module for AirBnB clone
"""

from models.base_model import BaseModel
from datetime import datetime

class Place(BaseModel):
    """
    Beginning stage of Place class

    Attributes:
        city_id (str):          city id
        user_id (str):          user id
        name (str):             place name
        description (str):      place description
        number_rooms (int):     number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int):        maximum number of guests
        price_by_night (int):   price per night
        latitude (float):       latitude
        longitude (float):      longitude
        amenity_ids (list):     list of amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, **kwargs):
        if not kwargs:
            super().__init__()
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