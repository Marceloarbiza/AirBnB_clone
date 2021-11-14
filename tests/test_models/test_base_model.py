#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_basemodel(self):
        """ test BaseModel """

        obj_bm = BaseModel()

        self.assertEqual(obj_bm.__class__, BaseModel)
        self.assertTrue(hasattr(obj_bm, 'id'), True)
        self.assertEqual(type(obj_bm.id), str)
        self.assertTrue(hasattr(obj_bm, 'created_at'), True)
        self.assertEqual(type(obj_bm.created_at), datetime)
        self.assertTrue(hasattr(obj_bm, 'updated_at'), True)
        self.assertEqual(type(obj_bm.updated_at), datetime)
        self.assertTrue(type(obj_bm.to_dict()), dict)

    def test_ids(self):
        """ test differente objects """

        obj_bm_1 = BaseModel()
        obj_bm_2 = BaseModel()

        self.assertEqual(type(obj_bm_1), type(obj_bm_2))
        self.assertNotEqual(obj_bm_1.id, obj_bm_2.id)

        id_2 = obj_bm_2.id

        obj_bm_2.id = '1234'

        self.assertEqual(obj_bm_2.id, '1234')

    def test_to_dict(self):
        """Test to_dict() method of BaseClass """
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertIn("my_number", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_str(self):

        obj_bm_3 = BaseModel()
        str_obj_3 = str(obj_bm_3)
        str_compare = '[{}] ({}) {}'.format(
                type(obj_bm_3).__name__, obj_bm_3.id, obj_bm_3.__dict__)

        self.assertEqual(str_obj_3, str_compare)

    def test_doc(self):
        """Docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_save(self):
        """ test save method`"""
        obj_bm_5 = BaseModel()
        created_at_1 = obj_bm_5.created_at
        updated_at_1 = obj_bm_5.updated_at
        obj_bm_5.save()
        created_at_2 = obj_bm_5.created_at
        updated_at_2 = obj_bm_5.updated_at
        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)
