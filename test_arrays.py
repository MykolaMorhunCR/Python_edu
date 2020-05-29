import unittest
import Tasks23
import numpy as np


class TestArr(unittest.TestCase):

    def test_max(self):
        self.assertNotEqual(maximum_values[0], Tasks23.maximum(main_array).maximum_values[1])
