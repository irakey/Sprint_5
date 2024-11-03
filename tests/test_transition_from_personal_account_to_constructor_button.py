from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_transition_from_personal_account_to_constructor_button(driver, user_email, user_password):
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

    constructor_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
    )
    constructor_button.click()

    constructor_heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.text_type_main-large"))
    )

    assert constructor_heading.is_displayed(), "Не удалось перейти на страницу конструктора из личного кабинета."
    print("Тест пройден: успешный переход в конструктор из личного кабинета.")
