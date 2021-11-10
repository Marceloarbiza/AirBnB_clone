#!/usr/bin/python3
""" Write all those classes that inherit from BaseModel """


from models.base_model import BaseModel


class State(BaseModel):
    """ Public class attributes """
    name = ''

    def __init__(self, *args, **kwargs):
        """ inherit from BaseModel """
        super().__init__(*args, **kwargs)
