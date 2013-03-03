
import py.test
import os
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base test class. All other test classes derive from this one
    """

    @classmethod
    def setup_class(self):
        self.browser = 'chrome'
        self.landingPage = "www.google.com"
        
        # should be abstracted to its own method, setupWebDriver
        if self.browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser.lower() == 'chrome':
            chromedriver = "/home/josh/programming/selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver =  webdriver.Chrome(chromedriver)
        else:
            raise RuntimeError("Invalid browser selection, try again")

        self.loadLandingPage()

    @classmethod
    def tearDown_class(self):
        self.driver.quit()

    @classmethod
    def loadLandingPage(self):
        self.driver.get(self.landingPage)
    
    def setupWebDriver(self):
        pass
