import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_transition_to_personal_account(user_email, user_password):
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_field.send_keys(user_email)

        password_field = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_field.send_keys(user_password)

        submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )

        personal_account_button = driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']")
        personal_account_button.click()

        profile_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']"))
        )

        assert profile_header.is_displayed(), "Переход в личный кабинет не выполнен."

        print("Тест пройден: переход в личный кабинет выполнен успешно.")

    except Exception as e:
        print(f"Тест завершился ошибкой: {e}")
    finally:
        driver.quit()
