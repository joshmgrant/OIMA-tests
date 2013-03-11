
import py.test
import os
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base test class. All other test classes derive from this one
    """

    def __init__(self):
        self.browser = 'chrome'
        self.landingpage = "http://www.oima-amio.ca"

    def setup_class(self):
        self.browser = 'firefox'
        self.landingpage = "http://www.oima-amio.ca"
             
        # should be abstracted to its own method, setupWebDriver
        if self.browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser.lower() == 'chrome':
            chromedriver = "/home/josh/programming/selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)
        else:
            raise RuntimeError("Invalid browser selection, try again")

        self.driver.get(self.landingpage)

    def teardown_class(self):
        self.driver.quit()

    def loadLandingPage(self, page_url):
        self.driver.get(page_url)

    def setupWebDriver(self, browser):
        if browser.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser.lower() == 'chrome':
            chromedriver = "/home/josh/programming/selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            return webdriver.Chrome(chromedriver)
        else:
            raise RuntimeError("Invalid browser selection, try again")
