
from AbstractPage import AbstractPage
from selenium import webdriver

class BasePage(AbstractPage):
    """
    Base class for each page
    """

    def __init__(self, driver):
        self.driver = driver

    def getExpectedPageName():
        raise NotImplementedError("getExpectedPageName() not implemented")
