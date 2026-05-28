#!/usr/bin/env python3
"""This module defines mixin classes and a Dragon class."""


class SwimMixin:
    """Provides swimming behavior."""

    def swim(self):
        """Prints a swimming message."""

        print("The creature swims!")


class FlyMixin:
    """Provides flying behavior."""

    def fly(self):
        """Prints a flying message."""

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon with swimming and flying abilities."""

    def roar(self):
        """Prints a roaring message."""

        print("The dragon roars!")
