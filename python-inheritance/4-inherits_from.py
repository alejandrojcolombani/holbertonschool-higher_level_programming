#!/usr/bin/python3
"""This module contains a function that checks inherited instances."""


def inherits_from(obj, a_class):
    """Returns True if obj inherits from a_class, otherwise False."""

    return isinstance(obj, a_class) and type(obj) is not a_class
