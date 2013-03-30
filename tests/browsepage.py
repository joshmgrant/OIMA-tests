from BasePage import BasePage
from selenium import webdriver
from random import randint
import requests
import logging

from selenium.common.exceptions import NoSuchElementException

locators = {'homeLink':'//a[@href=\'/en\']',
            'browseLink':'//a[@href=\'/en/browse\']', 
            'communityLink':'//a[@href=\'/en/community\']',
            'resourceLink':'//a[@href=\'/en/resources\']', 
            'blogLink':'//a[@href=\'/en/blog\']', 
            'aboutLink':'//a[@href=\'/en/page/about-us\']', 
            'contactLink':'//a[@href=\'/en/contact\']', 
            'blankResults':'//div[@class=\'empty-view\']', 
            'pageList':'//ul[@class=\'pager\']'}

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

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

    def followRandomLink(self):
        browse_links = self.driver.find_elements_by_xpath('//a[contains(@href, \'/browse/music/results?f[0]\')]')

        rand_link = randint(0,len(browse_links)-1)
        browse_links[rand_link].click()

        if self.driver.find_elements_by_xpath(locators['pageList']):
            pages = self.driver.find_elements_by_xpath(locators['pageList'] + '/li/a')
            rand_page = randint(0, len(pages)-1)
            pages[rand_page].click()

        self.waitPageLoad("Browse music")
    
    def findSongLinkStatus(self):
        
        if self.driver.find_elements_by_xpath(locators['blankResults']):
            log.info("Link produced no results")
            return
            
        play_list = self.driver.find_elements_by_partial_link_text("Play")    
               
        if play_list:
            r = requests.get(play_list[0].get_attribute("href"))
            return r.status_code
        else:
            raise NoSuchElementException("No play links found")

    def findAddToPlayList(self):
        if self.driver.find_elements_by_xpath(locators['blankResults']):
            log.info("Link produced no results")
            return

        add_list = self.driver.find_elements_by_partial_link_text("Add to play")
        
        if add_list:
            r = requests.get(add_list[0].get_attribute("href"))
            return r.status_code
        else:
            raise NoSuchElementException("No add to play list links found")

    def findDownloadList(self):
        if self.driver.find_elements_by_xpath(locators['blankResults']):
            log.info("Link produced no results")
            return

        dl_list = self.driver.find_elements_by_partial_link_text("Download")
        
        if dl_list:
            r = requests.get(dl_list[0].get_attribute("href"))
            return r.status_code
        else:
            raise NoSuchElementException("No download links found")
