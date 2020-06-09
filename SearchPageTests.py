import unittest
import test_UI.test_testClass


class UITestClass(unittest.TestCase):

    def test_searchTest(self):
        print("sdaf")
        gp = test_UI.test_testClass.GoooglePage()
        gp.openPage()
        gp.searchQuery("google")
