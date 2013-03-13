from BaseTest import BaseTest
from homepage import HomePage
import pytest

class HomePageTest(BaseTest):
    """
    tests for the home page
    """
    def setUp(self):
        self.driver = self.setup_webdriver()
    
    def tearDown(self):
        self.close()

    def test_title(self):
        h = HomePage(self.driver)
        self.quit_webdriver()
