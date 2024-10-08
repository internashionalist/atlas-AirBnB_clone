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
    # def setUp(self):
    #     """
    #     SetUp for Review class
    #     """
    #     review = Review()
    #     review_dict = review.to_dict()

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
        self.assertEqual(type(review), Review)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_init_kwargs(self):
        review = Review(place_id='Floor', user_id='Bob', text='your uncle')
        self.assertEqual(review.place_id, 'Floor')
        self.assertEqual(review.user_id, 'Bob')
        self.assertEqual(review.text, 'your uncle')

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

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        new_review = Review()
        review_dict = new_review.to_dict()
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_save(self):
        """
        Test for save method
        """
        new_review = Review()
        old_updated_at = new_review.updated_at
        new_review.save()
        self.assertNotEqual(old_updated_at, new_review.updated_at)

if __name__ == '__main__':
    unittest.main()