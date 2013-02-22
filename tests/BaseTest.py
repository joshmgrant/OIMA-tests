
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base test class. All other test classes derive from this one
    """

    @classmethod
    def startBrowser(self):
        self.driver = webdriver.Firefox()
        self.landingPage = 'http://oima-aimo.ca'

    def setUp(self):
        self.driver.get(landingPage)

    @classmethod
    def closeBrowser(self):
        self.driver.quit()

    def aTest(self):
        print 'run this test'
