#!/usr/bin/python3
"""This module contains a function that prints a square."""


def print_square(size):
    """Prints a square using the # character."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
