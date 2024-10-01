#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test for State class
    """
    def setUp(self):
        """
        SetUp for State class
        """
        OK = State()

    def tearDown(self):
        """
        TearDown for State class
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """
        Test for init method
        """
        OK = State()
        self.assertEqual(type(OK), State)
        self.assertEqual(OK.name, "")


if __name__ == '__main__':
    unittest.main()