#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_float_numbers(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_same_numbers(self):
        """Test with identical numbers."""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_string_list(self):
        """Test with strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_positions(self):
        """Test max at beginning."""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_at_end(self):
        """Test max at end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)


if __name__ == "__main__":
    unittest.main()