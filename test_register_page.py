from test_base import BaseTest
from pages.page_home import HomePage
from pages.page_register import RegisterPage
import unittest
import os
import csv
from ddt import ddt, data, unpack

# download data from the file invalid_emails.csv
def get_data(file_name):
    rows = []
    data_file = open(file_name, "rt")
    reader = csv.reader(data_file)
    # skip the first row
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


@ddt
class RegistrationTest(BaseTest):
    """
    Registration page tests
    """

    @data(*get_data("invalid_emails.csv"))
    @unpack
    def test_incorrect_email(
        self,
        name,
        surname,
        invalid_email,
        password,
        birthMonth,
        birthDay,
        birthYear,
        gender,
        pronoun,
    ):
        """Registration test - invalid e-mail"""
        # Home Page
        hp = HomePage(self.driver)
        hp._wait_for_cookies_btn()
        hp.click_cookies_btn()
        hp.click_registration_btn()
        hp._verify_page()
        # Register Page
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
