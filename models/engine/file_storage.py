#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return type(self).__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Serializes the objects to JSON and saves to file"""
        serialized_objs = {key: obj.to_dict() for key,
                           obj in type(self).__objects.items()}
        with open(type(self).__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes JSON file to objects"""
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    new_obj = cls(**value)
                    type(self).__objects[key] = new_obj

            except Exception:
                pass
