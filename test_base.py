import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    """
    This class contains th elements used by all tests,
    as setUP, tearDown.
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
