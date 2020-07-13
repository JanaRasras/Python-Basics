'''
'''

import unittest
from L25_Unit_Tests import circle_area
from math import pi

class TesrCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
        