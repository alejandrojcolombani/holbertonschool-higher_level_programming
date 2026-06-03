#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance.

        If attrs is a list of strings, only attributes whose names
        are included in attrs are returned.
        """
        if attrs is None:
            return self.__dict__

        student_dict = {}

        for key, value in self.__dict__.items():
            if key in attrs:
                student_dict[key] = value

        return student_dict
