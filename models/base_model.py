#!/usr/bin/python3
'''
Defines all common attributes/methods for other classes
'''

import uuid
from datetime import datetime

class BaseModel:
    '''
    Represent a base model.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initialize a new class
        id (string) : a uuid for the instance created
        created_at (datetime) : current datetime when an instance is created
        updated_at (datetime) : current datetime when an instance is updated
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'created_at':
                self.created_at = self.parse_datetime(value)
            elif key == 'updated_at':
                self.updated_at = self.parse_datetime(value)

    def parse_datetime(self, datetime_string):
        '''
        Parse a datetime string or return the current datetime if None
        datetime_string (str): Datetime string to parse
        '''
        if isinstance(datetime_string, datetime):
            return datetime_string
        elif datetime_string:
            return datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S.%f")
        return datetime.now()

    def __str__(self):
        '''
        Return a string representation of the instance
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Update the instance attribute updated_at with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of the instance
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
