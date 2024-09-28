#!/usr/bin/python3
"""
Place class module for AirBnB clone
"""

from models.base_model import BaseModel


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
    def __init__(self):
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
