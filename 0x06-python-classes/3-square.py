#!/usr/bin/python3

"""
create a class named Square that define a square by
private instance attribute: size
and a Public instance method that returns
the current square area
"""


class Square:
    """

        istantiation of size
        if size os less than 0, raise a ValueError
        exception with the message
        size must be >=0
    """

    def __init__(self, size=0):
        #   check for integers
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        #   check size
        if size < 0:
            raise ValueError("size must be >=0")

        self.__size = size

    def area(self):
        """
        Calculates area of square
        Returns: area
        """

        return (self.__size ** 2)
