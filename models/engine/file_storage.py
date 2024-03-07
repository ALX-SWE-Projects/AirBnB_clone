#!/usr/bin/python3
'''
Defines JSON file
'''

import json

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
        new_obj = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_obj, file)

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
