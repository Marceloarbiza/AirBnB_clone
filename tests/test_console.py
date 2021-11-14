#!/usr/bin/python3


import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os
import re


class TestAirbnb_Console(unittest.TestCase):
    """ test to class FileStorage """

    """ ____________ Test create ____________ """

    def test_create_missing_name(self):
        """ test create command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_dexist_name(self):
        """ test create command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_dexist_name(self):
        """ test create command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            pattern = "^[a-z0-9-]*$"
            self.assertTrue(bool(re.match(pattern, f.getvalue())))
