
from AbstractPage import AbstractPage
from selenium import webdriver
import pytest

class BasePage():
    """
    Base class for each page
    """

    def __init__(self, driver):
        self.driver = driver

    def getExpectedPageName():
        raise NotImplementedError("getExpectedPageName() not implemented")
