from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import USER_EMAIL, USER_PASSWORD, URL
from locators import TestLocators


class TestLogin:

    def test_login_from_main_page_button(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(USER_EMAIL)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(USER_PASSWORD)

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER_BUTTON))

        assert order_button.is_displayed()

        driver.quit()

    def test_login_from_password_recovery_form(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.RECOVER_PASSWORD_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_RECOVERY_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(
            USER_EMAIL)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.CREATE_ORDER_BUTTON))

        assert order_button.is_displayed()
        driver.quit()

    def test_login_from_personal_account_button(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(
            USER_EMAIL)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.CREATE_ORDER_BUTTON))

        assert order_button.is_displayed()
        driver.quit()

    def test_login_from_registration_form(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON_TEXT)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_RECOVERY_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(
            USER_EMAIL)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.CREATE_ORDER_BUTTON))

        assert order_button.is_displayed()
        driver.quit()
