#!/usr/bin/python3
'''
Defines JSON file
'''

import json
from models.base_model import BaseModel

class FileStorage:
    '''
    Represent a file storage system.
    __file_path (string): path to the file
    __objects (dictionary): all objects by <class name>.id
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id
        '''
        self.__objects[obj.id] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path)
        '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = {}

        new_obj = {}
        for key, value in self.__objects.items():
            if isinstance(value, BaseModel):
                new_obj[key] = value.to_dict()

        existing_data.update(new_obj)

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file)

    def reload(self):
        '''
        Deserializes __objects from the JSON file (path: __file_path if exists)
        '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                if data:
                    self.__objects = json.loads(data)
                else:
                    self.__objects = {}
        except FileNotFoundError:
            self.__objects = {}
