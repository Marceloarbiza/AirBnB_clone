#!/usr/bin/python3

from models.base_model import BaseModel
import json

listclass = {'BaseModel': BaseModel}
"""
listclass = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}
"""
class FileStorage:
    def __init__(self):
        self.__file_path = './file.json'
        self.__objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        name = type(obj).__name__
        idName = str(obj.id)
        nameF = name + '.' + idName
        self.__objects[nameF] = obj.to_dict()

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w') as fp:
            print('PRIMER DICT')
            print(self.__objects)
            print('****************')
            json.dump(self.__objects, fp)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open( self.__file_path, 'r') as f:
                obj = json.loads(f.read())
            for i in obj:
                self.__objects[i] = listclass[obj[i]["__class__"]](**obj[i])
        except:
            pass

