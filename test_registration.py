from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_custom_email
from data import URL, USER_PASSWORD
from locators import TestLocators


class TestRegistration:

    def test_registration_error_for_invalid_password(self, generate_custom_email, driver):

        driver.get(URL)

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON_TEXT)).click()

        driver.find_element(*TestLocators.NAME_INPUT).send_keys("Irina")

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(generate_custom_email)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("123")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON)).click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.WRONG_PASSWORD_ERROR))

        assert "Некорректный пароль" in error_message.text
        driver.quit()

    def test_successful_registration_with_valid_data(self, driver, generate_custom_email):
        driver.get(URL)

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON_TEXT)).click()

        driver.find_element(*TestLocators.NAME_INPUT).send_keys("Irina")

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(generate_custom_email)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)

        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()
        driver.quit()
