import unittest
from tasks import Lucky


class TestLucky(unittest.TestCase):

    def test_lucky(self):
        self.assertEqual(Lucky.lucky(6), 55252)
        self.assertEqual(Lucky.lucky(4), 670)
        with self.assertRaises(ValueError):
            Lucky.lucky(-10)
        with self.assertRaises(ValueError):
            Lucky.lucky(0)
        with self.assertRaises(ValueError):
            Lucky.lucky(7)
        with self.assertRaises(ValueError):
            Lucky.lucky(7777777777777777777777772)
        with self.assertRaises(TypeError):
            Lucky.lucky("string")
        with self.assertRaises(TypeError):
            Lucky.lucky(None)
        with self.assertRaises(TypeError):
            Lucky.lucky(True)
        with self.assertRaises(TypeError):
            Lucky.lucky([2, 3, 4])
        # with self.assertRaises(ValueError):
        #     Lucky.lucky(0)
        #     Lucky.lucky(-100)
        #     Lucky.lucky(7)
        #     Lucky.lucky(7777777777777777777777772)
        # with self.assertRaises(TypeError):
        #     Lucky.lucky("string")
        #     Lucky.lucky(6)
        #     Lucky.lucky(None)
