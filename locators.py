from selenium.webdriver.common.by import By

class HomePageLocators():
    COOKIES_BTN = (By.XPATH, '//button[@data-cookiebanner="accept_button"]')
    REGISTRATION_BTN = (By.XPATH, '//a[@data-testid="open-registration-form-button"]')

class RegisterPageLocators():
    NAME_INPUT = (By.NAME, "firstname")
    SURNAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "reg_email__")
    EMAIL_CONFIRMATION =(By.NAME, "reg_email_confirmation__")
    PASSWORD_INPUT = (By.NAME, "reg_passwd__")
    BIRTH_MONTH = (By.NAME, "birthday_month")
    BIRTH_DAY = (By.NAME, "birthday_day")
    BIRTH_YEAR = (By.NAME, "birthday_year")
    GENDER_FEMALE_BTN = (By.XPATH, '//input[@class="_8esa"][@value="1"]')
    GENDER_MALE_BTN = (By.XPATH, '//input[@class="_8esa"][@value="2"]')
    GENDER_CUSTOM_BTN = (By.XPATH, '//input[@class="_8esa"][@value="-1"]')
    PRONOUN = (By.NAME, "preferred_pronoun")
    SING_UP_BTN = (By.NAME, "websubmit")
    # REGISTRATION ERRORS
    MISSING_NAME = (By.XPATH, '//div[@class="_5v-0 _53im"]/div[contains(text(), "What’s your name?")]')
    MISSING_SURNAME = (By.XPATH, '//div[@class="_5v-0 _53il"]/div[contains(text(), "What’s your name?")]')
    WRONG_EMAIL = (By.XPATH, '//*[contains(text(), "Please enter a valid mobile number or email address.")]')
    WRONG_PASSWORD = (By.XPATH, '//*[contains(text(), "Enter a combination of at least six numbers, letters and punctuation marks (like ! and &).")]')
    WRONG_BIRTHDAY = (By.XPATH, '//*[contains(text(), "It looks like you entered the wrong info. Please be sure to use your real birthday.")]')
    MISSING_GENDER = (By.XPATH, '//*[contains(text(), "Please choose a gender. You can change who can see this later.")]')
