#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test for FileStorage class
    """
    def setUp(self):
        """
        SetUp for FileStorage class
        """
        self.storage = FileStorage()
        storage_dict = self.storage.all()

    def tearDown(self):
        """
        TearDown for FileStorage class
        """
        del self.storage

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_all(self):
        """
        Test for all method
        """
        self.assertTrue(isinstance(self.storage.all(), dict))

    def test_new(self):
        """
        Test for new method
        """
        storage = FileStorage()
        storage.new(BaseModel())
        self.assertTrue(isinstance(storage.all(), dict))

    def test_save(self):
        """
        Test for save method
        """
        storage = FileStorage()
        storage.save()
        self.assertTrue(isinstance(storage.all(), dict))

    def test_reload(self):
        """
        Test for reload method
        """
        storage = FileStorage()
        storage.reload()
        self.assertTrue(isinstance(storage.all(), dict))