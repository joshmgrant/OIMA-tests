from BasePage import BasePage
from selenium import webdriver

locators = {'browseLink':'//a[@href=\'/en/browse\']', 
            'homeLink':'//a[@href=\'/en\']'}

class HomePage(BasePage):
    """
    Home page for OIMA
    """

    def getExpectedPageName(self):
        return 'Ontario Independent Music Archive'

    def goToBrowseArchive(self):
        self.driver.find_element_by_xpath(locators['browseLink']).click()
        self.waitPageLoad("Browse music")
