import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ Set up the test environment """
        self.storage = FileStorage()
        self.model_instance = BaseModel()

    def tearDown(self):
        """ Clean up after the test """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_instance_creation(self):
        """ Test if FileStorage instance is created """
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_method(self):
        """ Test the all() method """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """ Test the new() method """
        key = "{}.{}".format(
                type(self.model_instance).__name__, self.model_instance.id
                )
        self.assertNotIn(key, storage.all())
        self.storage.new(self.model_instance)
        self.assertIn(key, storage.all())

    def test_save_method(self):
        """ Test the save() method """
        key = "{}.{}".format(
                type(self.model_instance).__name__, self.model_instance.id
                )
        self.model_instance.name = "Test Model"
        self.storage.new(self.model_instance)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as file:
            file_content = file.read()
            self.assertIn(key, file_content)
            self.assertIn("Test Model", file_content)

    def test_reload_method(self):
        """ Test the reload() method """
        key = "{}.{}".format(
                type(self.model_instance).__name__, self.model_instance.id
                )
        self.model_instance.name = "Test Model"
        self.storage.new(self.model_instance)
        self.storage.save()
        storage.reload()
        all_objects = storage.all()
        self.assertIn(key, all_objects)
        reloaded_instance = all_objects[key]
        self.assertEqual(reloaded_instance.name, "Test Model")


if __name__ == '__main__':
    unittest.main()
