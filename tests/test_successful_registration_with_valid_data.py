from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_successful_registration_with_valid_data(driver, generate_custom_email):
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"))
    ).click()

    driver.find_element(By.NAME, "name").send_keys("Irina")

    email_field = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    email_field.send_keys(generate_custom_email)

    password_field = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    password_field.send_keys("12345ABC")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))
    )
    print("Тест успешной регистрации прошел успешно.")

