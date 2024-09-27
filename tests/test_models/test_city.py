#!/usr/bin/python3
"""
Unittest for City class
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test for City class
    """
    def setUp(self):
        """
        SetUp for City class
        """
        self.city = City()
        city_dict = self.city.to_dict()

    def tearDown(self):
        """
        TearDown for City class
        """
        del self.city

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.city, BaseModel))

    def test_city_name(self):
        """
        Test for name input
        """
        city = City()
        city.name = "Tulsa"
        self.assertEqual(city.name, "Tulsa")

    def test_state_id(self):
        """
        Test for state_id input
        """
        city = City()
        city.state_id = "OK"
        self.assertEqual(city.state_id, "OK")
