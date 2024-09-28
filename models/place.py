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
    def __init__(self, *args, **kwargs):
        if not kwargs:
            super().__init__()
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
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