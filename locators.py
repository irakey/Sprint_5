from selenium.webdriver.common.by import By


class TestLocators:

    TAB_BUNS = By.XPATH, "//span[text()='Булки']" #Таб "Булки"
    ACTIVE_TAB_BUNS = By.XPATH, "//main/section[1]/div[1]/div[1]" #Активный таб "Булки"
    TAB_FILLINGS = By.XPATH, "//span[text()='Начинки']" #Таб "Начинки"
    ACTIVE_TAB_FILLINGS = By.XPATH, "//main/section[1]/div[1]/div[3]" #Активный таб "Начинки"
    TAB_SAUCES = By.XPATH, "//span[text()='Соусы']"#Таб "Соусы"
    ACTIVE_TAB_SAUCES = By.XPATH, "//main/section[1]/div[1]/div[2]" #Активный таб "Соусы"
    LOGIN_ACCOUNT_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']" #Кнопка 'Войти в аккаунт'
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/following-sibling::input" #Инпут ввода почты
    PASSWORD_INPUT = By.XPATH, "//label[text()='Пароль']/following-sibling::input"#Инпут ввода пароля
    LOGIN_BUTTON = By.XPATH, "//button[contains(@class, 'button') and text()='Войти']"#Кнопка "Войти"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"#Кнопка "Оформить заказ"
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"#Кнопка "Восстановить пароль"
    REGISTER_BUTTON_TEXT = By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"#Кнопка-текст "Зарегистрироваться"
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']"#Кнопка "Выход"
    WRONG_PASSWORD_ERROR = By.XPATH, "//p[contains(text(),'Некорректный пароль')]"#Ошибка 'Некорректный пароль'
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"#Кнопка "Конструктор"
    CONSTRUCTOR_ACTIVE = By.CSS_SELECTOR, "h1.text_type_main-large"#Активный "Конструктор"
    BURGER_HEADER = By.XPATH, "//h1[text()='Соберите бургер']"#Заголовок 'Соберите бургер'
    LOGO_IMAGE = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']" #Лого сайта
    LOGIN_RECOVERY_BUTTON = By.XPATH, "//a[contains(text(),'Войти')]" #Кнопка входа на экране восстановления пароля
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']" #Кнопка "Личный кабинет"
    NAME_INPUT = By.NAME, "name" #Инпут для ввода имени
    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']" #Кнопка "Зарегистрироваться"
    PROFILE_BUTTON = By.XPATH, "//a[@href='/account/profile']" #Кнопка "Профиль"
