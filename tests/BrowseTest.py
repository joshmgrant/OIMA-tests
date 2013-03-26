from BaseTest import BaseTest
from homepage import HomePage
from browsepage import BrowsePage
import unittest
import pytest
from time import sleep

class BrowsePageTest(BaseTest, unittest.TestCase):
    """
    tests for the home page
    """

    def test_browseLink(self):
        h = HomePage(self.driver)
        h.goToBrowseArchive()

    def test_playingRandomTrack(self):
        b = BrowsePage(self.driver)
        
        b.goToHere()
        b.followRandomLink()
        assert b.findSongLinkStatus() == 200
        
        
