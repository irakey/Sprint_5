# Проект автоматизации тестирования Stellar Burgers

Этот проект содержит автоматизированные тесты для сайта [Stellar Burgers](https://stellarburgers.nomoreparties.site/). Тесты написаны с использованием библиотеки `Selenium` для Python и предназначены для проверки различных сценариев использования, таких как регистрация, вход в аккаунт, переходы между разделами и работа с разделом «Конструктор».

## Структура тестов

Тесты сгруппированы по сценариям использования и включают следующие категории:

### 1. Регистрация

- **test_successful_registration_with_valid_data.py**: проверяет успешную регистрацию с корректными данными.
- **test_registration_error_for_invalid_password.py**: проверяет отображение ошибки при регистрации с некорректным паролем.

### 2. Вход

- **test_login_from_main_page_button.py**: тестирует вход через кнопку «Войти в аккаунт» на главной странице.
- **test_login_from_personal_account_button.py**: тестирует вход через кнопку «Личный кабинет».
- **test_login_from_registration_form.py**: тестирует вход через кнопку в форме регистрации.
- **test_login_from_password_recovery_form.py**: тестирует вход через кнопку в форме восстановления пароля.

### 3. Переход в личный кабинет

- **test_transition_to_personal_account.py**: проверяет переход в личный кабинет по кнопке «Личный кабинет».

### 4. Переход из личного кабинета в конструктор

- **test_transition_from_personal_account_to_constructor_button.py**: проверяет переход из личного кабинета в конструктор по кнопке «Конструктор».
- **test_transition_from_personal_account_to_constructor_logo.py**: проверяет переход из личного кабинета в конструктор по клику на логотип Stellar Burgers.

### 5. Выход из аккаунта

- **test_logout_from_personal_account.py**: проверяет выход из аккаунта по кнопке «Выйти» в личном кабинете.

### 6. Раздел «Конструктор»

- **test_constructor_buns_section_transition.py**: тестирует переход в раздел «Булки» конструктора.
- **test_constructor_sauces_section_transition.py**: тестирует переход в раздел «Соусы» конструктора.
- **test_constructor_fillings_section_transition.py**: тестирует переход в раздел «Начинки» конструктора.

## Установка и запуск тестов

Для запуска всех тестов выполните команду:
pytest -v

### Предварительные требования

Для работы проекта необходимы:
- Python 3.7 или новее
- Установленный WebDriver (например, ChromeDriver для Google Chrome)
- Установленный пакет `pytest` и `selenium`

### Установка зависимостей

Установите зависимости с помощью команды:

```bash
pip install -r requirements.txt

