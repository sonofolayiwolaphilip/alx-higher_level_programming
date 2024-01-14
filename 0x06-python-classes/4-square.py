#!/usr/bin/python3

"""
create a class named Square that define a square by
private instance attribute: size
and a Public instance method that returns
the current square area
Methods Getter and Setter properties for size.
property def size(self): to retrieve property
"""


class Square:
    """
    instantiating the variables self and size
    Raising errors if conditions are not met
    """
    def __init__(self, size=0):
        # Initialize private attribute
        self.__size = size

    @property  # property to retrieve size
    def size(self):
        return self.__size

    @size.setter    # Setter method for size
    def size(self, value):
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        #   check if value is >= 0
        if value < 0:
            raise ValueError("size must be >= 0")

        # Update the private instance attribute
        self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns: area
        """
        return (self.__size ** 2)