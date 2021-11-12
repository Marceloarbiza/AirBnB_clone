#!/usr/bin/python3

import unittest
from model.base_model import BaseModel

class TestAirbnb(unittest.TestCase):

    def test_basemodel(self):

        obj_bm_1 = BaseModel()
        self.assertEqual(obj_bm_1.__class__, BaseModel)
        self.assertEqual(type(obj_bm_1.id), str)

if __name__ == '__main__':
    unittest.main()
