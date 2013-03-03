from BaseTest import BaseTest

class HomePageTest(BaseTest):
    """
    tests for the home page
    """

    def test_title(self):
        self.driver.get("www.oima-amio.ca/en")
