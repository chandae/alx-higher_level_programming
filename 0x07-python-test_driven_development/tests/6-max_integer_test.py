#!/usr/bin/python3
"""
    Unittest Module for 6-max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([10]), 10)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertAlmostEqual(max_integer([2, 5, 3, 1, 4]), 5)
        self.assertAlmostEqual(max_integer([-1, -5, -3, -10]), -1)
        self.assertAlmostEqual(max_integer([-12, 2, -7, -3, 6]), 6)
    
    def test_non_int(self):
        self.assertRaises(TypeError, max_integer, True)
