#!/usr/bin/python3
"""Create a console whith cmd"""


import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import cmd
#from shlex import split

listclass = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

class HBNBCommand(cmd.Cmd):
    """Comands to cmd"""
    prompt = '(hbnb) '
    listArg = []

    # ----- basic hbnb commands -----
    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return(1)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return(1)

    def emptyline(self):
        """ pass line """
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        listArg = arg.split(' ')
        if listArg[0] == '':
            print('** class name missing **')
        elif listArg[0] not in listclass:
            print("** class doesn't exist **")
        elif (listArg[0] in listclass) and len(listArg) == 1:
            print('** instance id missing **')
        elif len(listArg) == 2:
            compare = (listArg[0] + '.' + listArg[1])
            if compare in models.storage.all():
                print(models.storage.all()[compare])
            else:
                print('** no instance found **')
        else:
            pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        listArg = arg.split(' ')
        if listArg[0] == '':
            print('** class name missing **')
        elif listArg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif listArg[0] == 'BaseModel' and len(listArg) == 1:
            objBM = BaseModel()
            objBM.save()
            print(objBM.id)
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        pass

    def do_all(self, arg):
        """v"""
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
