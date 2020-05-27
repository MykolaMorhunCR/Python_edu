import unittest
import Lucky


class TestArr(unittest.TestCase):

    def test_lucky_positive(self):
        self.assertEqual(Lucky.lucky(6), 55252)
        self.assertEqual(Lucky.lucky(4), 670)

        with self.assertRaises(ValueError):
            Lucky.lucky("string")
