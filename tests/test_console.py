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

    def test_create_exist_name(self):
        """ test create command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            pattern = "^[a-z0-9-]*$"
            self.assertTrue(bool(re.match(pattern, f.getvalue())))

    """ ____________ Test show ____________ """

    def test_show_missing_name(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_show_dexist_name(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_missing_id(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_show_corect_id(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            bm_id = f.getvalue()
            str_show = '{} {} {}'.format('show', 'BaseModel', bm_id)
        with patch('sys.stdout', new=StringIO()) as f:            
            HBNBCommand().onecmd(str_show)
            pattern = "[a-zA-Z0-9-:',[{}_()]"
            self.assertTrue(bool(re.match(pattern, f.getvalue())))

    """ ____________ Test destroy ____________ """

    def test_destroy_missing_name(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_destroy_dexist_name(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy_missing_id(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy_incorect_id(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    """ ____________ Test all ____________ """

    def test_all_incorrect_name(self):
        """ test all command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_correct(self):
        """ test all command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertTrue(f.getvalue())

    def test_all_correct_class(self):
        """ test all command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue(f.getvalue())

    """ ____________ Test update ____________ """
    
    """
    def test_update_missing_name(self):

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
    """

    def test_update_dexist_name(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update_missing_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_update_incorect_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 121212")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_update_corect_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            bm_id = f.getvalue()
            str_show = '{} {} {}'.format('update', 'BaseModel', bm_id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(str_show)
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")

    """            
    def test_update_corect_id(self):

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            bm_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel " + bm_id + " first_name")
            self.assertEqual(f.getvalue(), "** value missing **\n")
    
    def test_update_correct(self):

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            bm_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel " + bm_id + "first_name Franquito")
            HBNBCommand().onecmd("show BaseModel " + bm_id)
            self.assertTrue("Franquito" in f.getvalue())
    """

    """ ____________ Test User _____________ """

    def test_user_create_exist_name(self):
        """ test create command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            pattern = "^[a-z0-9-]*$"
            self.assertTrue(bool(re.match(pattern, f.getvalue())))

    def test_user_show_missing_id(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_user_show_corect_id(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            bm_id = f.getvalue()
            str_show = '{} {} {}'.format('show', 'User', bm_id)
        with patch('sys.stdout', new=StringIO()) as f:            
            HBNBCommand().onecmd(str_show)
            pattern = "[a-zA-Z0-9-:',[{}_()]"
            self.assertTrue(bool(re.match(pattern, f.getvalue())))

    def test_user_destroy_missing_id(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_user_destroy_incorect_id(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 121212")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_user_all_correct_class(self):
        """ test all command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertTrue(f.getvalue())

    def test_user_update_missing_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_user_update_incorect_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 121212")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_user_update_corect_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            bm_id = f.getvalue()
            str_show = '{} {} {}'.format('update', 'User', bm_id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(str_show)
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")

    """ ____________ Test State _____________ """

    def test_state_create_exist_name(self):
        """ test create command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            pattern = "^[a-z0-9-]*$"
            self.assertTrue(bool(re.match(pattern, f.getvalue())))

    def test_state_show_missing_id(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_state_show_corect_id(self):
        """ test show command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            bm_id = f.getvalue()
            str_show = '{} {} {}'.format('show', 'State', bm_id)
        with patch('sys.stdout', new=StringIO()) as f:            
            HBNBCommand().onecmd(str_show)
            pattern = "[a-zA-Z0-9-:',[{}_()]"
            self.assertTrue(bool(re.match(pattern, f.getvalue())))

    def test_state_destroy_missing_id(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_state_destroy_incorect_id(self):
        """ test destroy command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State 121212")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_state_all_correct_class(self):
        """ test all command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertTrue(f.getvalue())

    def test_state_update_missing_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_state_update_incorect_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State 121212")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_user_update_corect_id(self):
        """ test update command """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            bm_id = f.getvalue()
            str_show = '{} {} {}'.format('update', 'State', bm_id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(str_show)
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")

    """ ____________ Test Count _____________ """

    def test_count(self):
        """ test count command """
    
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            num_ini = int(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(int(f.getvalue()), num_ini + 1)
