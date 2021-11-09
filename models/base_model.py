#!/usr/bin/python3

#from models.__init__ import storage
import uuid
from datetime import datetime

class BaseModel:
    """ Write a class BaseModel that defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        from models.__init__ import storage
        if kwargs is not None and len(kwargs) >= 1:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__> """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        from models.__init__ import storage
        self.updated_at = datetime.today()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dicRet = self.__dict__
        dicRet['__class__'] = self.__class__.__name__
        dicRet['created_at'] = str(self.created_at.isoformat())
        dicRet['updated_at'] = str(self.updated_at.isoformat())
        return dicRet
