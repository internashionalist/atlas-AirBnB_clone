#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
import os
from models.place import Place
from models.base_model import BaseModel



class TestPlace(unittest.TestCase):
    """
    Test for Place class
    """
    def setUp(self):
        """
        SetUp for Place class
        """
        self.place = Place()
        place_dict = self.place.to_dict()

    def tearDown(self):
        """
        TearDown for Place class
        """
        del self.place
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.place, BaseModel))

    def test_city_id(self):
        """
        Test for city_id input
        """
        place = Place()
        place.city_id = "Tulsa"
        self.assertEqual(place.city_id, "Tulsa")

    def test_user_id(self):
        """
        Test for user_id input
        """
        place = Place()
        place.user_id = "jackflash"
        self.assertEqual(place.user_id, "jackflash")

    def test_name(self):
        """
        Test for name input
        """
        place = Place()
        place.name = "Loft"
        self.assertEqual(place.name, "Loft")

    def test_description(self):
        """
        Test for description input
        """
        place = Place()
        place.description = "This is a sick loft."
        self.assertEqual(place.description, "This is a sick loft.")

    def test_number_rooms(self):
        """
        Test for number_rooms input
        """
        place = Place()
        place.number_rooms = 4
        self.assertEqual(place.number_rooms, 4)

    def test_number_bathrooms(self):
        """
        Test for number_bathrooms input
        """
        place = Place()
        place.number_bathrooms = 2
        self.assertEqual(place.number_bathrooms, 2)

    def test_max_guest(self):
        """
        Test for max_guest input
        """
        place = Place()
        place.max_guest = 5
        self.assertEqual(place.max_guest, 5)

    def test_price_by_night(self):
        """
        Test for price_by_night input
        """
        place = Place()
        place.price_by_night = 275
        self.assertEqual(place.price_by_night, 275)

    def test_latitude(self):
        """
        Test for latitude input
        """
        place = Place()
        place.latitude = 123.456
        self.assertEqual(place.latitude, 123.456)

    def test_longitude(self):
        """
        Test for longitude input
        """
        place = Place()
        place.longitude = 789.101
        self.assertEqual(place.longitude, 789.101)

    def test_amenity_ids(self):
        """
        Test for amenity_ids input
        """
        place = Place()
        place.amenity_ids = ["wifi", "pool", "fireplace"]
        self.assertEqual(place.amenity_ids, ["wifi", "pool", "fireplace"])

if __name__ == '__main__':
    unittest.main()