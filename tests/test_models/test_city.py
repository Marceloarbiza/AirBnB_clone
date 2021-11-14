#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.city import City
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_city_class(self):
        """ test correct atributes of the class """
        obj_ci = City()

        self.assertEqual(obj_ci.__class__, City)

    def test_city_id(self):
        """ test correct atributes of the class """
        obj_ci = City()

        self.assertTrue(hasattr(obj_ci, 'id'), True)
        self.assertEqual(type(obj_ci.id), str)

    def test_city_created_at(self):
        """ test correct atributes of the class """
        obj_ci = City()

        self.assertTrue(hasattr(obj_ci, 'created_at'), True)
        self.assertEqual(type(obj_ci.created_at), datetime)

    def test_city_updated_at(self):
        """ test correct atributes of the class """
        obj_ci = City()

        self.assertTrue(hasattr(obj_ci, 'updated_at'), True)
        self.assertEqual(type(obj_ci.updated_at), datetime)


    def test_city_name(self):
        """ test correct atributes of the class """
        obj_ci = City()

        self.assertTrue(hasattr(obj_ci, 'name'), True)
        self.assertEqual(type(obj_ci.name), str)

    def test_city_state(self):
        """ test correct atributes of the class """
        obj_ci = City()

        self.assertTrue(hasattr(obj_ci, 'state_id'), True)
        self.assertEqual(type(obj_ci.state_id), str)

    def test_city_dict(self):
        """ test correct atributes of the class """
        obj_ci = City()

        self.assertTrue(type(obj_ci.to_dict()), dict)

    def test_city_to_dict(self):
        """ test the objet in dictionary representation like method to_dict """
        obj_ci = City()
        obj_ci_d = obj_ci.to_dict()

        self.assertEqual(obj_ci_d["__class__"], "City")
        self.assertEqual(type(obj_ci_d["id"]), str)
        self.assertEqual(type(obj_ci_d["created_at"]), str)
        self.assertEqual(type(obj_ci_d["updated_at"]), str)
        self.assertTrue(type(obj_ci_d), dict)
        self.assertNotEqual(obj_ci_d, obj_ci.__dict__)
    

    def test_ids(self):
        """ test differente objects ids """
        obj_ci_1 = City()
        obj_ci_2 = City()

        self.assertEqual(type(obj_ci_1), type(obj_ci_2))
        self.assertNotEqual(obj_ci_1.id, obj_ci_2.id)

        id_2 = obj_ci_2.id

        obj_ci_2.id = '1234'

        self.assertEqual(obj_ci_2.id, '1234')

    def test_to_dict(self):
        """Test to_dict() method of BaseClass """
        model = City()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertIn("my_number", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "City")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_str(self):
        """ test the string representation of the object """
        obj_ci_3 = City()
        str_obj_3 = str(obj_ci_3)
        str_compare = '[{}] ({}) {}'.format(
                type(obj_ci_3).__name__, obj_ci_3.id, obj_ci_3.__dict__)

        self.assertEqual(str_obj_3, str_compare)

    def test_doc(self):
        """Docstring"""
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.save.__doc__)
        self.assertIsNotNone(City.to_dict.__doc__)
        self.assertIsNotNone(City.__str__.__doc__)

    def test_save(self):
        """ test save method`"""
        obj_ci_5 = City()

        created_at_1 = obj_ci_5.created_at
        updated_at_1 = obj_ci_5.updated_at
        
        obj_ci_5.save()

        created_at_2 = obj_ci_5.created_at
        updated_at_2 = obj_ci_5.updated_at

        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_stored(self):
        """ test correct storage """
        obj_ci_6 = City()
        self.assertIn(obj_ci_6, models.storage.all().values())

