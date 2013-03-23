
from AbstractPage import AbstractPage
from selenium import webdriver
from selenium.webdriver.support import ui
import pytest

class BasePage():
    """
    Base class for each page
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = ui.WebDriverWait(self.driver, 10)

    def getExpectedPageName(self):
        raise NotImplementedError("getExpectedPageName() not implemented")

    def waitPageLoad(self, page_title):
        self.wait.until(lambda driver: page_title in driver.title)
