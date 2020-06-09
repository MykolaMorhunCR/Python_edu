import unittest
import Tasks23
import numpy as np


class TestArr(unittest.TestCase):

    def test_max(self):
        main_array = np.random.randint(-1000, high=1000, size=1000)
        maxx = Tasks23.maximum(main_array)
        self.assertNotEqual(maxx[0], maxx[1])
    def test_