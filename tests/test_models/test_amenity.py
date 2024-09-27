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
        """
        SetUp for Amenity class
        """
        self.amenity = Amenity()
        amenity_dict = self.amenity.to_dict()

    def tearDown(self):
        """
        TearDown for Amenity class
        """
        del self.amenity

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.amenity, BaseModel))

    def test_name(self):
        """
        Test for name input
        """
        amenity = Amenity()
        amenity.name = "Fireplace"
        self.assertEqual(amenity.name, "Fireplace")
