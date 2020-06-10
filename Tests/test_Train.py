import unittest
from tasks import Trian


class TestTriangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rectangular = Trian.Triangle(3, 4, 5)
        cls.isosceles = Trian.Triangle(6, 6, 10)
        cls.equilateral = Trian.Triangle(10, 10, 10)
        cls.miscellaneous = Trian.Triangle(23, 15, 17)
        return cls.rectangular, cls.isosceles, cls.equilateral, cls.miscellaneous

    def test_perimeter(self):
        self.assertEqual(self.miscellaneous.compute_perimeter(), 55)
        self.assertEqual(self.equilateral.compute_perimeter(), 30)
        self.assertEqual(self.isosceles.compute_perimeter(), 22)
        self.assertEqual(self.rectangular.compute_perimeter(), 12)

    def test_area(self):
        self.assertEqual(self.miscellaneous.compute_area(), 127.44484100974822)
        self.assertEqual(self.equilateral.compute_area(), 43.30127018922193)
        self.assertEqual(self.isosceles.compute_area(), 16.583123951777)
        self.assertEqual(self.rectangular.compute_area(), 6)

    def test_type(self):
        self.assertEqual(self.miscellaneous.type(), "miscellaneous")
        self.assertEqual(self.equilateral.type(), "equilateral")
        self.assertEqual(self.isosceles.type(), "isosceles")
        self.assertEqual(self.rectangular.type(), "rectangular")

# class TriangleNegative(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         print("123123123")
#         cls.impossible = Triangle("ter", 4, 5)
#         return cls.impossible
#
#     def test_raise(self):
#         print("123123")
#         with self.assertRaises(ValueError):
#             self.impossible.__init__()
