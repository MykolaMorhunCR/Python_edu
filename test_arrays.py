import unittest
import Tasks23
import numpy as np


class TestArr(unittest.TestCase):

    def setUp(self):
        main_array = np.random.randint(-1000, high=1000, size=1000)
        return main_array

    def test_max(self):
        self.assertNotEqual(Tasks23.maximum(self.main_array).maximum_values[0], Tasks23.maximum().maximum_values[1])
