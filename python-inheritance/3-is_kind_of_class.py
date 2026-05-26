#!/usr/bin/python3
"""This module contains a function that checks object inheritance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from, a_class."""

    return isinstance(obj, a_class)
