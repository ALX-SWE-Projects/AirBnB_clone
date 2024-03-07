#!/usr/bin/python3

'''
Import necessary modules/classes to expose them when the package is imported
'''

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
