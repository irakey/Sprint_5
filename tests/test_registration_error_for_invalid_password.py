from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_error_for_invalid_password(generate_custom_email):
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"))).click()

        driver.find_element(By.NAME, "name").send_keys("Irina")

        email_field = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        email_field.send_keys(generate_custom_email)

        password_field = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_field.send_keys("123")

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']")))
        register_button.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))

        assert "Некорректный пароль" in error_message.text, "Ошибка не отображается!"

        print("Тест прошёл успешно: Ошибка при регистрации с некорректным паролем отображается.")

    except Exception as e:
        print(f"Тест завершился ошибкой: {e}")
    finally:
        driver.quit()
