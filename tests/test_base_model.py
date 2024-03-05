'''Tests for the BaseModel class'''

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''Test case for the BaseModel class'''

    def test_init(self):
        '''Test initialization'''

        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

        id_value = "test_id"
        created_at_value = datetime(2023, 3, 5, 12, 30, 0)
        updated_at_value = datetime(2023, 3, 5, 12, 35, 0)
        obj = BaseModel(id=id_value, created_at=created_at_value, updated_at=updated_at_value)
        self.assertEqual(obj.id, id_value)
        self.assertEqual(obj.created_at, created_at_value)
        self.assertEqual(obj.updated_at, updated_at_value)

    def test_save(self):
        '''Test that save method updates updated_at attribute'''

        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict(self):
        '''Test that to_dict method returns a dictionary with expected keys and values'''

        obj = BaseModel()
        obj_dict = obj.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(obj_dict.keys(), expected_keys)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
