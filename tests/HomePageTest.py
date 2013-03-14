from BaseTest import BaseTest
from homepage import HomePage
import unittest
import pytest
from time import sleep

class HomePageTest(unittest.TestCase, BaseTest):
    """
    tests for the home page
    """
    #def setUp(self):
    #    setUp(self)

    #def tearDown(self):
    #    super.tearDown(self)

    def test_title(self):
        h = HomePage(self.driver)
        print "got here"
        sleep(3)
        self.driver.quit()
