#!/usr/bin/env python3
"""This module defines Animal classes using abstraction."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Represents an abstract animal."""

    @abstractmethod
    def sound(self):
        """Returns the sound made by the animal."""
        pass


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Returns the dog sound."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Returns the cat sound."""
        return "Meow"
