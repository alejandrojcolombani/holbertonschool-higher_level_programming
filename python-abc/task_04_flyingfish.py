#!/usr/bin/env python3
"""This module defines animal classes using multiple inheritance."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Prints a swimming message."""

        print("The fish is swimming")

    def habitat(self):
        """Prints the fish habitat."""

        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Prints a flying message."""

        print("The bird is flying")

    def habitat(self):
        """Prints the bird habitat."""

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish."""

    def fly(self):
        """Prints a flying fish flying message."""

        print("The flying fish is soaring!")

    def swim(self):
        """Prints a flying fish swimming message."""

        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the flying fish habitat."""

        print("The flying fish lives both in water and the sky!")
