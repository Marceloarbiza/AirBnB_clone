#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.state import State
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_state_class(self):
        """ test correct atributes of the class """
        obj_st = State()

        self.assertEqual(obj_st.__class__, State)

    def test_state_id(self):
        """ test correct atributes of the class """
        obj_st = State()

        self.assertTrue(hasattr(obj_st, 'id'), True)
        self.assertEqual(type(obj_st.id), str)

    def test_state_created_at(self):
        """ test correct atributes of the class """
        obj_st = State()

        self.assertTrue(hasattr(obj_st, 'created_at'), True)
        self.assertEqual(type(obj_st.created_at), datetime)

    def test_state_updated_at(self):
        """ test correct atributes of the class """
        obj_st = State()

        self.assertTrue(hasattr(obj_st, 'updated_at'), True)
        self.assertEqual(type(obj_st.updated_at), datetime)

    def test_state_name(self):
        """ test correct atributes of the class """
        obj_st = State()

        self.assertTrue(hasattr(obj_st, 'name'), True)
        self.assertEqual(type(obj_st.name), str)

    def test_state_dict(self):
        """ test correct atributes of the class """
        obj_st = State()

        self.assertTrue(type(obj_st.to_dict()), dict)

    def test_state_to_dict(self):
        """ test the objet in dictionary representation like method to_dict """
        obj_st = State()
        obj_st_d = obj_st.to_dict()

        self.assertEqual(obj_st_d["__class__"], "State")
        self.assertEqual(type(obj_st_d["id"]), str)
        self.assertEqual(type(obj_st_d["created_at"]), str)
        self.assertEqual(type(obj_st_d["updated_at"]), str)
        self.assertTrue(type(obj_st_d), dict)
        self.assertNotEqual(obj_st_d, obj_st.__dict__)

    def test_ids(self):
        """ test differente objects ids """
        obj_st_1 = State()
        obj_st_2 = State()

        self.assertEqual(type(obj_st_1), type(obj_st_2))
        self.assertNotEqual(obj_st_1.id, obj_st_2.id)

        id_2 = obj_st_2.id

        obj_st_2.id = '1234'

        self.assertEqual(obj_st_2.id, '1234')

    def test_to_dict(self):
        """Test to_dict() method of BaseClass """
        model = State()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertIn("my_number", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "State")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_str(self):
        """ test the string representation of the object """
        obj_st_3 = State()
        str_obj_3 = str(obj_st_3)
        str_compare = '[{}] ({}) {}'.format(
                type(obj_st_3).__name__, obj_st_3.id, obj_st_3.__dict__)

        self.assertEqual(str_obj_3, str_compare)

    def test_doc(self):
        """Docstring"""
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.save.__doc__)
        self.assertIsNotNone(State.to_dict.__doc__)
        self.assertIsNotNone(State.__str__.__doc__)

    def test_save(self):
        """ test save method`"""
        obj_st_5 = State()

        created_at_1 = obj_st_5.created_at
        updated_at_1 = obj_st_5.updated_at

        obj_st_5.save()

        created_at_2 = obj_st_5.created_at
        updated_at_2 = obj_st_5.updated_at

        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_stored(self):
        """ test correct storage """
        obj_st_6 = State()
        self.assertIn(obj_st_6, models.storage.all().values())
