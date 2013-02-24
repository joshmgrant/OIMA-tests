
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base test class. All other test classes derive from this one
    """

    def __init__(self, browser):
        self.browser = browser
        self.landingPage = 'http://oima-aimo.ca'

    @classmethod
    def setupClass(self):
        self.driver = self.setupWebDriver()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def loadLandingPage(self):
        self.driver.get(self.landingPage)
    
    def setupWebDriver(self):
        if browser.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser.lower() == 'chrome':
            return webdriver.Chrome()
        else:
            raise RuntimeError("Invalid browser selection, try again")
