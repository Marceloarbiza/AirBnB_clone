#!/usr/bin/python3

import models
import uuid
from datetime import datetime


class BaseModel:
    """
        Write a class BaseModel that defines all
        common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ class constructor """
        if kwargs is not None and len(kwargs) >= 1:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, 'created_at') and
            isinstance(self.created_at, str):
                self.created_at = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if hasattr(self, 'updated_at') and
            isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__> """
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
#        storage.new(self)
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dicRet = dict(self.__dict__)
        dicRet['__class__'] = self.__class__.__name__
        dicRet['created_at'] = self.created_at.isoformat()
        dicRet['updated_at'] = self.updated_at.isoformat()
        return dicRet
