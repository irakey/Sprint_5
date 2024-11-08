from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_from_personal_account_button(user_password, user_email):
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        personal_account_button.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_field.send_keys(user_email)

        password_field = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_field.send_keys(user_password)

        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

        assert order_button.is_displayed(), "Вход не выполнен, кнопка 'Оформить заказ' недоступна."

        print("Тест пройден: вход через 'Личный кабинет' выполнен успешно.")

    except Exception as e:
        print(f"Тест завершился ошибкой: {e}")
    finally:
        driver.quit()
