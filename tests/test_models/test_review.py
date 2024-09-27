#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest
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
        self.review = Review()
        review_dict = self.review.to_dict()

    def tearDown(self):
        """
        TearDown for Review class
        """
        del self.review

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.review, BaseModel))

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
