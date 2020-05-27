import unittest
import Lucky

class TestArr(unittest.TestCase):

    def test_lucky(self):
        self.assertEqual(Lucky.lucky(6), 55252)
        self.assertEqual(Lucky.lucky(4), 670)

        with self.assertRaises(ValueError):
            Lucky.lucky("string")
            Lucky.lucky(0)
            Lucky.lucky(-100)
            Lucky.lucky(7)
            Lucky.lucky(7777777777777777777777772)
