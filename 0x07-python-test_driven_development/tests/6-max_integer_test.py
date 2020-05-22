#!/usr/bin/python3
"""
Unittest max_integer([])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([2]), 2)

    def test_max(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([1, 2, 100, 5, 6]), 100)

    def test_string(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer(["aa", "cc", "bb"]), "cc")

    def test_float(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([0.10, 0.20, 0.8, 0.30, 0.40]), 0.8)

    def test_integer_float(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([1.5, 1, 2.5, 2, 8.5, 8]), 8.5)

    def test_negative_integer(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([-2, -6, -1, -100, -52, -64, -9]), -1)

    def test_negative_float(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([-2.5, -6.5, -1.5, -100.5, -52.5,
                                      -64.5, -9.5]), -1.5)

    def test_positive_negative(self):
        """
        Unittest max_integer([])
        """
        self.assertEqual(max_integer([5, -5, 1, -1, 100, -100, 0,
                                      -0, 9, -9]), 100)


if __name__ == '__main__':
    unittest.main()
