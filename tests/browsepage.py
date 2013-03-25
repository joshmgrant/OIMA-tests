from BasePage import BasePage
from selenium import webdriver

locators = {'homeLink':'//a[@href=\'/en\']',
            'browseLink':'//a[@href=\'/en/browse\']', 
            'communityLink':'//a[@href=\'/en/community\']',
            'resourceLink':'//a[@href=\'/en/resources\']', 
            'blogLink':'//a[@href=\'/en/blog\']', 
            'aboutLink':'//a[@href=\'/en/page/about-us\']', 
            'contactLink':'//a[@href=\'/en/contact\']'}

class BrowsePage(BasePage):
    """
    Home page for OIMA
    """

    def goToHere(self):    
        self.driver.get("http://oima-amio.ca/en/browse")
        self.waitPageLoad("Browse music")

    def getExpectedPageName(self):
        return 'Browse music|Ontario Independent Music Archive'

    def goToHomePage(self):
        self.driver.find_element_by_xpath(locators['homeLink']).click()
        self.waitPageLoad("Ontario Independent Music Archive")

        return HomePage(self.driver)

    def searchArchive(self, terms):
        search_box = self.driver.find_element_by_id("edit-s")
        search_button = self.driver.find_element_by_id("edit-submit-browse")

        search_box.send_keys(terms)
        search_button.click()

        self.waitPageLoad("Browse music")

               
