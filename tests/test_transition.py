from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import USER_EMAIL, USER_PASSWORD, URL
from locators import TestLocators


class TestTransition:

    def test_transition_from_personal_account_to_constructor_button(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(USER_EMAIL)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON)).click()

        constructor_heading = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.CONSTRUCTOR_ACTIVE))

        assert constructor_heading.is_displayed()

    def test_transition_from_personal_account_to_constructor_logo(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(
            USER_EMAIL)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGO_IMAGE)).click()

        header_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BURGER_HEADER))
        assert header_text.is_displayed()

    def test_transition_to_personal_account(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(
            USER_EMAIL)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        profile_header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON))

        assert profile_header.is_displayed()
