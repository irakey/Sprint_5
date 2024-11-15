from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import USER_EMAIL, USER_PASSWORD, URL
from locators import TestLocators


class TestLogout:

    def test_logout_from_personal_account(self, driver):
        driver.get(URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(USER_EMAIL)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()

        login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        assert login_button.is_displayed()
