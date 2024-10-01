#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test for Review class
    """
    def setUp(self):
        """
        SetUp for Review class
        """
        review = Review()
        review_dict = self.review.to_dict()

    def tearDown(self):
        """
        TearDown for Review class
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """
        Test for init method
        """
        review = Review()
        self.assertIsEqual(type(review), Review)

    def test_place_id(self):
        """
        Test for place_id input
        """
        review = Review()
        review.place_id = "314"
        self.assertEqual(review.place_id, "314")

    def test_user_id(self):
        """
        Test for user_id input
        """
        review = Review()
        review.user_id = "777"
        self.assertEqual(review.user_id, "777")

    def test_text(self):
        """
        Test for text input
        """
        review = Review()
        review.text = "This place is a mansion!"
        self.assertEqual(review.text, "This place is a mansion!")

if __name__ == '__main__':
    unittest.main()