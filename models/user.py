#!/usr/bin/python3
""" Class user """
from models.base_model import BaseModel


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_user_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
