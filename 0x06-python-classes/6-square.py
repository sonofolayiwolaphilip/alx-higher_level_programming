#!/usr/bin/python3

"""
class Square that defines a square
Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:

Private instance attribute: position
which takes a default (0, 0) tuple.
property def position(self): to retrieve it
property setter def position(self, value): to set it:

And a Public instance method: def area(self):
that returns the current square area
Method my_print prints the square using "#".
"""


class Square:
    """
    Instantiate the variables self and size.
    raising error if conditions are not met.
    and print square using '#'.
    """
    def __init__(self, size=0, position=(0, 0)):
        # Initialize private attributes
        self.size = size
        self.postion = position

    @property  # propert to retrieve size
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method that sets the size of square.
        Args:
            value (int): size of Square
        Raises:
            TyprError: if value is not an integer.
            ValueError: If value is less than 0.

        """
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check if value is an integer
        if value < 0:
            raise ValueError("size must be >= 0")

        # update the private instance attribute
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """position setter methon that sets position of Square.
        Args:
            value (tuple): tuple of two positive integer coordinates
        Raises:
            TypeError: IF value is not a tuple of two positive integers

        """
        # verify that is a tuple of 2 positive integers
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate area of square
        returns: area
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
