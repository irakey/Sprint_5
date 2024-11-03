import pytest
import random
from selenium import webdriver


@pytest.fixture
def generate_custom_email():
    first_name = "irina"
    last_name = "kurbanova"
    cohort_number = "15"
    random_digits = ''.join(random.choices("0123456789", k=3))
    return f"{first_name}_{last_name}_{cohort_number}_{random_digits}@ya.ru"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def user_email():
    return 'kurbanova_15@gmail.com'


@pytest.fixture
def user_password():
    return '12345ACB'

