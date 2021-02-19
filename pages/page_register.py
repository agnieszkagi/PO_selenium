from pages.page_base import BasePage
from locators import RegisterPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class RegisterPage(BasePage):

    def fill_name(self, name):
        el = self.driver.find_element(*RegisterPageLocators.NAME_INPUT)
        el.send_keys(name)

    def fill_surname(self, surname):
        el = self.driver.find_element(*RegisterPageLocators.SURNAME_INPUT)
        el.send_keys(surname)

    def fill_email(self, email):
        el = self.driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        el.send_keys(email)

    def fill_email_confirmation(self, email):
        # check if element EMAIL_CONFIRMATION is is_displayed
        # if yes, fill with the email value
        if self.driver.find_element(*RegisterPageLocators.EMAIL_CONFIRMATION).is_displayed():
            el = driver.find_element(*RegisterPageLocators.EMAIL_CONFIRMATION)
            el.send_keys(email)

    def fill_password(self, password):
        el = self.driver.find_element(*RegisterPageLocators.PASSWORD_INPUT)
        el.send_keys(password)

    def choose_birth_month(self, birthMonth):
        el = Select(self.driver.find_element(*RegisterPageLocators.BIRTH_MONTH))
        el.select_by_value(birthMonth)

    def choose_birth_day(self, birthDay):
        el = Select(self.driver.find_element(*RegisterPageLocators.BIRTH_DAY))
        el.select_by_value(birthDay)

    def choose_birth_year(self, birthYear):
        el = Select(self.driver.find_element(*RegisterPageLocators.BIRTH_YEAR))
        el.select_by_value(birthYear)

    def choose_gender(self, gender):
        if gender == "M":
            # choose male
            el = self.driver.find_element(*RegisterPageLocators.GENDER_MALE_BTN)
            el.click()
        elif gender == "F":
            # choose female
            el = self.driver.find_element(*RegisterPageLocators.GENDER_FEMALE_BTN)
            el.click()
        else:
            # choose custom
            self.driver.find_element(*RegisterPageLocators.GENDER_CUSTOM_BTN)
            el.click()

    def choose_pronoun(self, gender, pronoun):
        if gender not in ('F, ''M'):
            if pronoun == "she":
                value = '1'
            elif pronoun == "he":
                value = '2'
            else:
                value = '3'
            if gender not in("M", "F"):
                el = Select(self.driver.find_element(*RegisterPageLocators.PRONOUN))
                el.select_by_value(value)

    def choose_sing_up_btn(self):
        el = self.driver.find_element(*RegisterPageLocators.SING_UP_BTN)
        el.click()


    def verify_if_reg_error_occurs(self, number_of_errors, type_of_errors):
        """
        The fuction verifies every invidual field by clikcing on it and
        looking for error message. If error message is displayed the error count
        increases.
        """
        visible_error_notices = []
        #NAME
        self.driver.find_element(*RegisterPageLocators.NAME_INPUT).click()
        if len(self.driver.find_elements(*RegisterPageLocators.MISSING_NAME)) <= 0:
            print("name error text not displayed (not in page code)")
        else:
            if self.driver.find_element(*RegisterPageLocators.MISSING_NAME).is_displayed():
                visible_error_notices.append("missing_name")
                print("name error text is displayed")
            else:
                print("name error text not displayed")

        #SURNAME
        self.driver.find_element(*RegisterPageLocators.SURNAME_INPUT).click()
        if len(self.driver.find_elements(*RegisterPageLocators.MISSING_SURNAME)) <= 0:
            print("surname error text not displayed (not in page code)")
        else:
            if self.driver.find_element(*RegisterPageLocators.MISSING_SURNAME).is_displayed():
                print("surname error text is displayed")
                visible_error_notices.append("missing_surname")
            else:
                print("surname error text not displayed")

        #EMAIL
        self.driver.find_element(*RegisterPageLocators.EMAIL_INPUT).click()
        if len(self.driver.find_elements(*RegisterPageLocators.WRONG_EMAIL)) <= 0:
            print("email error text not displayed (not in page code)")
        else:
            if self.driver.find_element(*RegisterPageLocators.WRONG_EMAIL).is_displayed():
                print("email error text is displayed")
                visible_error_notices.append("wrong_email")
            else:
                print("email error text not displayed")
        #PASSWORD
        self.driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).click()
        if len(self.driver.find_elements(*RegisterPageLocators.WRONG_PASSWORD)) <= 0:
            print("password error text not displayed (not in page code)")
        else:
            if self.driver.find_element(*RegisterPageLocators.WRONG_PASSWORD).is_displayed():
                print("password error text is displayed")
                visible_error_notices.append("wrong_password")
            else:
                print("password error text not displayed")
        #BIRTHDAY
        self.driver.find_element(*RegisterPageLocators.BIRTH_MONTH).click()
        if len(self.driver.find_elements(*RegisterPageLocators.WRONG_BIRTHDAY)) <= 0:
            print("birthday error text not displayed (not in page code)")
        else:
            if self.driver.find_element(*RegisterPageLocators.WRONG_BIRTHDAY).is_displayed():
                print("birthday error text is displayed")
                visible_error_notices.append("wrong_bithday")
            else:
                print("birthday error text not displayed")
        #Gender
        if len(self.driver.find_elements(*RegisterPageLocators.MISSING_GENDER)) <= 0:
            print("gender error text not displayed (not in page code)")
        else:
            if self.driver.find_element(*RegisterPageLocators.MISSING_GENDER).is_displayed():
                print("gender error text is displayed")
                visible_error_notices.append("missing_gender")
            else:
                print("gender error text not displayed")

        # check if the correct number of errors is visible
        assert len(visible_error_notices) == number_of_errors
        # check if the correct error type is displayed
        assert visible_error_notices == type_of_errors
