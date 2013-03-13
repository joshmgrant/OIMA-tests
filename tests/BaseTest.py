
import py.test
import os
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base test class. All other test classes derive from this one
    """

    def __init__(self):
        unittest.TestCase.__init__(self)
        self.browser = 'chrome'
        self.landingpage = "http://www.oima-amio.ca"
        self.driver = self.setup_webdriver(self.browser)

    def load_landing_page(self, page_url):
        self.driver.get(page_url)
        
    def close(self):
        self.driver.quit()

    def open_webdriver(self, browser):
        if browser.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser.lower() == 'chrome':
            chromedriver = "/home/josh/programming/selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            return webdriver.Chrome(chromedriver)
        else:
            raise RuntimeError("Invalid browser selection, try again")
