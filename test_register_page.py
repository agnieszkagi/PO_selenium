from test_base import BaseTest
from pages.page_home import HomePage
from pages.page_register import RegisterPage
import unittest
import os
from time import sleep

class RegistrationTest(BaseTest):
    """
    Registration page tests
    """
    def test_incorrect_email(self, name='Ala', surname='Nowak', invalid_email='ala.com', password='aksu%1A', birthMonth='12', birthDay='12', birthYear='1990', gender='F', pronoun = None):
        """Registration test - invalid e-mail"""
        # Home Page
        hp = HomePage(self.driver)
        hp._wait_for_cookies_btn()
        hp.click_cookies_btn()
        hp.click_registration_btn()
        hp._verify_page()
        #Register Page
        rp = RegisterPage(self.driver)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.fill_email(invalid_email)
        rp.fill_email_confirmation(invalid_email)
        rp.fill_password(password)
        rp.choose_birth_month(birthMonth)
        rp.choose_birth_day(birthDay)
        rp.choose_birth_year(birthYear)
        rp.choose_gender(gender)
        rp.choose_pronoun(gender, pronoun)
        # Click Register btn DO NOT USE FOR THE POSITIVE CASE !!!!]
        rp.choose_sing_up_btn()
        # Verify if the displayed errors are correct
        rp.verify_if_reg_error_occurs(1, ["wrong_email"])

#testowe dane
name = 'Alicja'
surname = 'Nowak'
invalid_email = 'alanowak.com'
password = 'aguy4$G'
birthMonth = '12'
birthDay = '12'
birthYear = '1991'
gender = 'F'


if __name__=="__main__":
    unittest.main(verbosity=2)
