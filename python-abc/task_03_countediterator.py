#!/usr/bin/env python3
"""This module defines a CountedIterator class."""


class CountedIterator:
    """Represents an iterator that counts iterations."""

    def __init__(self, iterable):
        """Initializes the counted iterator."""

        self.iter = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Returns the iterator object."""
        return self

    def __next__(self):
        """Returns the next item and increments the counter."""

        item = next(self.iter)
        self.counter += 1

        return item

    def get_count(self):
        """Returns the number of iterated items."""
        return self.counter
