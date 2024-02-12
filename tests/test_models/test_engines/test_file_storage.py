#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class FileStorageTests(unittest.TestCase):
    """Suite of File Storage Tests"""

    def setUp(self):
        """Set up for each test case"""
        self.my_model = BaseModel()

    def tearDown(self):
        """Clean up after each test case"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def testStoreBaseModel(self):
        """Test save and reload functions"""
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """Test save, reload, and update functions"""
        self.my_model.my_name = "First name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "First name")

        create1 = bm_dict['created_at']
        update1 = bm_dict['updated_at']

        self.my_model.my_name = "Second name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = bm_dict['created_at']
        update2 = bm_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict['my_name'], "Second name")

    def testSaveSelf(self):
        """Check save self"""
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
