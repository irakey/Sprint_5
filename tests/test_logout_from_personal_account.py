from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout_from_personal_account(driver, user_email, user_password):
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
    ).send_keys(user_email)

    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
    )

    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(((By.XPATH, "//button[text()='Выход']")))
    ).click()

    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']"))
    )

    assert login_button.is_displayed(), "Выход из аккаунта не выполнен, кнопка 'Войти в аккаунт' не отображается."
    print("Тест пройден: выход из аккаунта выполнен успешно.")
