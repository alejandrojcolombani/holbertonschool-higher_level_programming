#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints the square using the # character."""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
