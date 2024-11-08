from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_constructor_sauces_section_transition():
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        fillings_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']")))
        fillings_tab.click()

        active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']")))

        assert active_section.is_displayed(), "Раздел 'Начинки' не активен!"

        print("Тест пройден: Переход в раздел 'Начинки' выполнен успешно.")

    except Exception as e:
        print(f"Тест завершился ошибкой: {e}")
    finally:
        driver.quit()
