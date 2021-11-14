#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.place import Place
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_place_class(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertEqual(obj_pl.__class__, Place)

    def test_place_id(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'id'), True)
        self.assertEqual(type(obj_pl.id), str)

    def test_place_created_at(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'created_at'), True)
        self.assertEqual(type(obj_pl.created_at), datetime)

    def test_place_updated_at(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'updated_at'), True)
        self.assertEqual(type(obj_pl.updated_at), datetime)

    def test_place_name(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'name'), True)
        self.assertEqual(type(obj_pl.name), str)

    def test_place_usr_id(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'user_id'), True)
        self.assertEqual(type(obj_pl.user_id), str)

    def test_place_city_id(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'city_id'), True)
        self.assertEqual(type(obj_pl.city_id), str)

    def test_place_description(self):
        """ test correct atributes of the class """
        obj_pl = Place()
        
        self.assertTrue(hasattr(obj_pl, 'description'), True)
        self.assertEqual(type(obj_pl.description), str)

    def test_numer_rooms(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'number_rooms'), True)
        self.assertEqual(type(obj_pl.number_rooms), int)

    def test_number_bathrooms(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'number_bathrooms'), True)
        self.assertEqual(type(obj_pl.number_bathrooms), int)

    def test_max_guest(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'max_guest'), True)
        self.assertEqual(type(obj_pl.max_guest), int)

    def test_price_by_night(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'price_by_night'), True)
        self.assertEqual(type(obj_pl.price_by_night), int)

    def test_latitude(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'latitude'), True)
        self.assertEqual(type(obj_pl.latitude), float)

    def test_longitude(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'longitude'), True)
        self.assertEqual(type(obj_pl.longitude), float)

    def test_amenity_ids(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(hasattr(obj_pl, 'amenity_ids'), True)
        self.assertEqual(type(obj_pl.amenity_ids), list)

    def test_place_dict(self):
        """ test correct atributes of the class """
        obj_pl = Place()

        self.assertTrue(type(obj_pl.to_dict()), dict)

    def test_place_to_dict(self):
        """ test the objet in dictionary representation like method to_dict """
        obj_pl = Place()
        obj_pl_d = obj_pl.to_dict()

        self.assertEqual(obj_pl_d["__class__"], "Place")
        self.assertEqual(type(obj_pl_d["id"]), str)
        self.assertEqual(type(obj_pl_d["created_at"]), str)
        self.assertEqual(type(obj_pl_d["updated_at"]), str)
        self.assertTrue(type(obj_pl_d), dict)
        self.assertNotEqual(obj_pl_d, obj_pl.__dict__)
    

    def test_ids(self):
        """ test differente objects ids """
        obj_pl_1 = Place()
        obj_pl_2 = Place()

        self.assertEqual(type(obj_pl_1), type(obj_pl_2))
        self.assertNotEqual(obj_pl_1.id, obj_pl_2.id)

        id_2 = obj_pl_2.id

        obj_pl_2.id = '1234'

        self.assertEqual(obj_pl_2.id, '1234')

    def test_to_dict(self):
        """Test to_dict() method of BaseClass """
        model = Place()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertIn("my_number", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "Place")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_str(self):
        """ test the string representation of the object """
        obj_pl_3 = Place()
        str_obj_3 = str(obj_pl_3)
        str_compare = '[{}] ({}) {}'.format(
                type(obj_pl_3).__name__, obj_pl_3.id, obj_pl_3.__dict__)

        self.assertEqual(str_obj_3, str_compare)

    def test_doc(self):
        """Docstring"""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.save.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)
        self.assertIsNotNone(Place.__str__.__doc__)

    def test_save(self):
        """ test save method`"""
        obj_pl_5 = Place()

        created_at_1 = obj_pl_5.created_at
        updated_at_1 = obj_pl_5.updated_at
        
        obj_pl_5.save()

        created_at_2 = obj_pl_5.created_at
        updated_at_2 = obj_pl_5.updated_at

        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_stored(self):
        """ test correct storage """
        obj_pl_6 = Place()
        self.assertIn(obj_pl_6, models.storage.all().values())

