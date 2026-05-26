#!/usr/bin/python3
"""This module defines a Square class."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square."""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the square."""

        return "[Rectangle] {}/{}".format(
            self.__size,
            self.__size
        )
