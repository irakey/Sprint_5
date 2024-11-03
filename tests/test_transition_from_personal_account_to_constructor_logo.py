from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_transition_from_personal_account_to_constructor_logo(driver, user_email, user_password):
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

    logo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"))
    )
    logo.click()

    header_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
    )

    assert header_text.is_displayed(), "Переход на главную страницу конструктора не выполнен."
    print("Тест пройден: переход в конструктор по клику на логотип выполнен успешно.")
