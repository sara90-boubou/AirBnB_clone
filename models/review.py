#!/usr/bin/python3
""" review module"""

from models.base_model import BaseModel


class Review:
    """Class representing reviews."""

    def __init__(self, text, rating, user_id, amenity_id):
        """Initialization of a Review instance.

        Args:
            - text: Text of the review
            - rating: Rating of the review
            - user_id: ID of the user who wrote the review
            - amenity_id: ID of the amenity being reviewed
        """
        self.text = text
        self.rating = rating
        self.user_id = user_id
        self.amenity_id = amenity_id

    def display_info(self):
        """Display information about the review."""
        print(f"Review Text: {self.text}")
        print(f"Rating: {self.rating}")
        print(f"User ID: {self.user_id}")
        print(f"Amenity ID: {self.amenity_id}")
