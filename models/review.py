#!/usr/bin/python3
""" Write all those classes that inherit from BaseModel """


from models.base_model import BaseModel


class Review(BaseModel):
    """ Public class attributes """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ inherit from BaseModel """
        super().__init__(*args, **kwargs)
