from pages.page_base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators

class HomePage(BasePage):
    def click_cookies_btn(self):
        el = self.driver.find_element(*HomePageLocators.COOKIES_BTN)
        el.click()

    def click_registration_btn(self):
        el = self.driver.find_element(*HomePageLocators.REGISTRATION_BTN)
        el.click()

    def _wait_for_cookies_btn(self):
        # Wait for cookies btn'
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.COOKIES_BTN))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.COOKIES_BTN))

    def _verify_page(self):
        # Verify if page title is correct
        # Wait for button 'Create New Account'
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.REGISTRATION_BTN))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.REGISTRATION_BTN))
        assert "Facebook - Log In or Sign Up" in self.driver.title
        print("HomePage verification")
