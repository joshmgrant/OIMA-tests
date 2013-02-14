from selenium import webdriver

class AbstractPage():
    """
    Abstract page object for use with testing.
    Contains webdriver initialization and general utility methods
    """
    
    def __init__(self, driver):
        self.driver = driver

    def getExpectedPageName():
        raise NotImplementedError("getExpectedPageName() not implemented")
