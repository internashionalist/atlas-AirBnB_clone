#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest
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
        self.state = State()
        state_dict = self.state.to_dict()

    def tearDown(self):
        """
        TearDown for State class
        """
        del self.state

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.state, BaseModel))

    def test_state_name(self):
        """
        Test for name input
        """
        state = State()
        state.name = "Oklahoma"
        self.assertEqual(state.name, "Oklahoma")

if __name__ == '__main__':
    unittest.main()