#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test for Amenity class
    """
    def setUp(self):
        self.amenity = Amenity()
        amenity_dict = self.amenity.to_dict()

    def tearDown(self):
        del self.amenity

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.amenity, BaseModel))
