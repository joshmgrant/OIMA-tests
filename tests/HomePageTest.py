from BaseTest import BaseTest
from homepage import HomePage
import unittest
import pytest
from time import sleep

class HomePageTest(BaseTest, unittest.TestCase):
    """
    tests for the home page
    """

    def test_title(self):
        h = HomePage(self.driver)
        print "got here"
        sleep(1)
        assert h.getExpectedPageName() == "Ontario Independent Music Archive"

    def test_fail(self):
        h = HomePage(self.driver)
        assert False
