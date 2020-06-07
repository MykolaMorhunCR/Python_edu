import unittest
import Trian


class TestTrian(unittest.TestCase):

    def test_lucky(self):
        self.assertEqual(Trian.Triangle.compute_perimeter(self), 12)
  #
