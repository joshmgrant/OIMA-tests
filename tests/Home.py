from BasePage import BasePage
from selenium import webdriver

class HomePage(BasePage):
    """
    Home page for OIMA
    """

    def getExpectedPageName(self):
        return 'Ontario Independent Music Archive'
