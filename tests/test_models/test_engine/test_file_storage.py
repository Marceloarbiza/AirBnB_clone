#!/usr/bin/python3

import unittest
import models
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class TestAirbnb_Storage(unittest.TestCase):
    """ test to class FileStorage """

    def test_fs_class(self):
        """ test the class of FileStorage """
        fs = FileStorage()

        self.assertEqual(fs.__class__, FileStorage)

    def test_fs_storage(self):
        """ test the class of storage """
        self.assertTrue(isinstance(models.storage, FileStorage))

    def test_fs_all(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'all'), True)

    def test_fs_new(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'new'), True)

    def test_fs_save(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'save'), True)

    def test_fs_reload(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'reload'), True)

    def test_exe_all(self):
        """ test methods """
        self.assertEqual(type(models.storage.all()), dict)

    def test_new_instance(self):
        """ test the creation of different instances """

        models.storage.new(BaseModel)
        models.storage.new(BaseModel)
        models.storage.new(BaseModel)
        models.storage.new(BaseModel)
        models.storage.new(BaseModel)
        models.storage.new(BaseModel)
        models.storage.new(BaseModel)
        models.storage.new(BaseModel)
