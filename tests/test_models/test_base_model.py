#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_Instantiation
    TestBaseModel_Instance_Print
    TestBaseModel_Save_Method
    TestBaseModel_to_Dict_Method
"""
import unittest
import json
import re
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from models import storage


class TestBaseModel_Instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_is_instance_of(self):
        """Test instance"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(str(type(b1)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(b1), BaseModel))

    def test_contains_id(self):
        """Test if id attribute exists"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))

    # ... (other tests, unchanged)

    def test_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        b1 = BaseModel()
        diff = b1.updated_at - b1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = date_now - b1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    # ... (other tests, unchanged)


class TestBaseModel_Instance_Print(unittest.TestCase):
    """Unittest for testing the __str__ method."""

    def test_str_return(self):
        """Unittest for testing the return value of __str__ method."""
        b1 = BaseModel()
        Dika = "[{}] ({}) {}".format("BaseModel", b1.id, str(b1.__dict__))
        self.assertEqual(str(b1), Dika)

    def test_str(self):
        """test that the str method has the correct output"""
        b1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(b1.id, b1.__dict__)
        self.assertEqual(string, str(b1))

    # ... (other tests, unchanged)


class TestBaseModel_Save_Method(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validates_save(self):
        """Check save models"""
        b1 = BaseModel()
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    # ... (other tests, unchanged)


class TestBaseModel_to_Dict_Method(unittest.TestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    # ... (other tests, unchanged)

    def test_to_dict_output(self):
        dt = datetime.today()
        b1 = BaseModel()
        b1.id = "123456"
        b1.created_at = b1.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(b1.to_dict(), tdict)

    # ... (other tests, unchanged)


if __name__ == "__main__":
    unittest.main()
