#!/usr/bin/env python3
"""This module defines a VerboseList class."""


class VerboseList(list):
    """Represents a list with verbose output."""

    def append(self, item):
        """Adds an item to the list and prints a message."""

        print("Added [{}] to the list".format(item))
        super().append(item)

    def extend(self, items):
        """Extends the list and prints a message."""

        print("Extended list with [{}] items".format(len(items)))
        super().extend(items)

    def remove(self, item):
        """Removes an item from the list and prints a message."""

        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns an item from the list."""

        item = self[index]

        print("Popped [{}] from the list".format(item))

        return super().pop(index)
