#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """ Write a class BaseModel that defines all common attributes/methods for other classes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__> """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dicRet = self.__dict__
        dicRet['__class__'] = self.__class__.__name__
        dicRet['created_at'] = str(self.created_at.isoformat())
        dicRet['updated_at'] = str(self.updated_at.isoformat())
        return dicRet

