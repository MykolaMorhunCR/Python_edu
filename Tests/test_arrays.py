import unittest
from tasks import array
import numpy as np


class TestArr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.perfect_array = array.Arrays(np.arange(0, 1000))
        cls.zero_array = array.Arrays(np.zeros(1000))

    def test_max(self):
        #print(len(main_array))
        maxx = array.Arrays.maximum(self.perfect_array)
        self.assertNotEqual(maxx[0], maxx[1])

    def test_bounds(self):
        self.assertCountEqual(np.arange(400, 600), array.Arrays.Bounds(self.perfect_array))

