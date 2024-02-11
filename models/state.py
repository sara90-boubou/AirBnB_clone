#!/usr/bin/python3
""" Class State """

from models.base_model import BaseModel


class State:
    """Class representing states."""

    def __init__(self, name):
        """Initialization of a State instance.

        Args:
            - name: Name of the state
        """
        self.name = name

    def display_info(self):
        """Display information about the state."""
        print(f"State Name: {self.name}")
