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
import cmd
import re

listclass = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}
notChangeThis = ['id', 'created_at', 'updated_up']

class HBNBCommand(cmd.Cmd):
    """Comands to cmd"""
    prompt = '(hbnb) '
    listArg = []

    # ----- basic hbnb commands -----
    def do_EOF(self):
        """Quit command to exit the program\n"""
        return(1)

    def do_quit(self):
        """Quit command to exit the program\n"""
        return(1)

    def emptyline(self):
        """ pass line """
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id\n"""
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
        pass


    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id\n"""
        listArg = arg.split(' ')
        if listArg[0] == '':
            print('** class name missing **')
        elif listArg[0] not in listclass:
            print("** class doesn't exist **")
        elif listArg[0] in listclass and len(listArg) == 1:
            objBM = listclass[listArg[0]]()
            objBM.save()
            print(objBM.id)
        pass


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)\n"""
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
                del (models.storage.all()[compare])
                #HAY QUE GUARDAR?
            else:
                print('** no instance found **')
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).\n"""
        listArg = arg.split(' ')
        if listArg[0] == '':
            print('** class name missing **')
        elif listArg[0] not in listclass:
            print("** class doesn't exist **")
        elif (listArg[0] in listclass) and len(listArg) == 1:
            print('** instance id missing **')
        else:
            compare = (listArg[0] + '.' + listArg[1])
            if (compare not in models.storage.all()):
                print('** no instance found **')
            elif len(listArg) == 2:
                print('** attribute name missing **')
            elif len(listArg) == 3:
                print('** value missing **')
            else:
                setattr(models.storage.all()[compare], listArg[2], listArg[3])
                models.storage.all()[compare].save()

#    def do_all(self, arg):
#        """ Prints all string representation of all instances based or not on the class name\n"""
#        listArg = arg.split(' ')
#        if (arg == ''):
#            for key in models.storage.all():
#                print(str(models.storage.all()[key]))
#        else:
#            if (listArg[0] not in listclass):
#                print("** class doesn't exist **")
#            elif len(listArg) == 1:
#                for value in models.storage.all().values():
#                    if value.__class__.__name__ == listArg[0]:
#                        print(str(value))
#        pass

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name\n """
        listP = []
        listArg = arg.split(' ')
        if (arg == ''):
            for k, v in models.storage.all().items():
                listP.append(str(v))
            print('['+','.join(listP)+']')
        else:
            if (listArg[0] not in listclass):
                print("** class doesn't exist **")
            elif listArg[0] in listclass:
                for k, v in models.storage.all().items():
                    if listArg[0] in k:
                        listP.append(str(models.storage.all()[k]))
                print('['+','.join(listP)+']')


    def do_count(self, arg):
        """ Count the argument """
        listArg = arg.split(' ')
        count = 0
        if arg == '()':
            print('** class name missing **')
        elif listArg[0] not in listclass:
            print("** class doesn't exist **")
        else:
            for instance, value in models.storage.all().items():
                if models.storage.all()[instance].__class__.__name__ == listArg[0]:
                    count += 1
            print(count)

    def default(self, arg):
        """ When the command prefix is not recognized call this method and change the words order for to try running with other method\n """
        try:
            """
            str_tmp = ''
            str_tmp = ' '.join(arg.replace('(','.').replace(')','').replace('"','').split('.'))
            list_tmp = str_tmp.split(' ')
            print('El string es: {}'.format(str_tmp))
            print(list_tmp)
            str_cmd = list_tmp[0] + ' ' + list_tmp[2]
            print('El string cmd: {}'.format(str_cmd))
            """

            listdef = []
            tmp = (re.split("[.(),]", arg))
            for i in tmp:
                if i != '':
                    if i[0:1] == '\"':
                        listdef.append(i[1:-1])
                    else:
                        listdef.append(i)
            del listdef[1]

            str_cmd = ' '.join(listdef)
            dicFuncs = {'all' : self.do_all,
                        'create' : self.do_create,
                        'show' : self.do_show,
                        'destroy' : self.do_destroy,
                        'update' : self.do_update,
                        'count' : self.do_count}
            #print(str_cmd)
            #return dicFuncs[list_tmp[1]](str_cmd)
            #print('++++++++++++++++++++++++++\n Funcion default \n+++++++++++++++++')
            print([tmp[1]], (str_cmd))
            return dicFuncs[tmp[1]](str_cmd)

        except:
            print('NO ENTRÓ')
            pass


if __name__ == '__main__':
        HBNBCommand().cmdloop()
