
import py.test
import os
import unittest
from selenium import webdriver

class BaseTest(object):
    """
    Base test class. All other test classes derive from this one
    """

    def setUp(self):
        self.browser = 'firefox'
        self.landingpage = "http://www.oima-amio.ca"        
        self.driver = self.setup_webdriver(self.browser)

        self.load_landing_page(self.landingpage)

    def load_landing_page(self, page_url):
        self.driver.get(page_url)
        
    def tearDown(self):
        self.driver.quit()

    def setup_webdriver(self, browser):
        if browser.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser.lower() == 'chrome':
            chromedriver = "/home/josh/programming/selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            return webdriver.Chrome(chromedriver)
        else:
            raise RuntimeError("Invalid browser selection, try again")
