#!/usr/bin/env python3
""" Class Amenity """


class Amenity:
    """Class representing amenities."""

    def __init__(self, name):
        """Initialization of an Amenity instance.

        Args:
            - name: Name of the amenity
        """
        self.name = name

    def display_info(self):
        """Display information about the amenity."""
        print(f"Amenity: {self.name}")

# Example usage:
if __name__ == "__main__":
    amenity_instance = Amenity("Swimming Pool")
    amenity_instance.display_info()
