from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_REG_NAME = (By.XPATH, '//fieldset[1]//input')  # Registration: input field "Имя"
    LOCATOR_REG_EMAIL = (By.XPATH, '//fieldset[2]//input')  # Registration: input field "Email"
    LOCATOR_REG_PASSWORD = (By.XPATH, '//fieldset[3]//input[@name="Пароль"]')  # Registration: input field "Пароль"
    LOCATOR_REG_BUTTON = (
        By.XPATH, '//button[text()="Зарегистрироваться"]')  # Registration: button "Зарегистрироваться"
    LOCATOR_REG_PASSWORD_ERROR = (
        By.XPATH, '//p[text()="Некорректный пароль"]')  # Registration: password validation error
    LOCATOR_REG_LOGIN_BUTTON = (By.XPATH, '//a[text()="Войти"]')  # Registration: button 'Войти'

    LOCATOR_MAIN_GOTO_ACC_BUTTON = (
        By.XPATH, '//button[text()="Войти в аккаунт"]')  # Main page: button "Войти в аккаунт"
    LOCATOR_MAIN_MAKE_ORDER = (
        By.XPATH, '//button[text()="Оформить заказ"]')  # Main page, logged-in user: button "Оформить заказ"
    LOCATOR_MAIN_MY_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Main page: button "Личный Кабинет"

    LOCATOR_MAIN_BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]')  # Main page: section "Булки"
    LOCATOR_MAIN_BUNS_CHECK_SELECTED_STATE = (
        By.XPATH, '//span[text()="Булки"]/parent::div')  # Main page: section "Булки" -> parent div
    LOCATOR_MAIN_SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')  # Main page: section "Соусы"
    LOCATOR_MAIN_SAUCES_CHECK_SELECTED_STATE = (
        By.XPATH, '//span[text()="Соусы"]/parent::div')  # Main page: section "Соусы" -> parent div
    LOCATOR_MAIN_FILINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')  # Main page: section "Начинки"
    LOCATOR_MAIN_FILINGS_CHECK_SELECTED_STATE = (
        By.XPATH, '//span[text()="Начинки"]/parent::div')  # Main page: section "Начинки" -> parent div

    LOCATOR_LOGIN_EMAIL = (By.XPATH, '//fieldset[1]//input')  # Login: input field "Email"
    LOCATOR_LOGIN_PASSWORD = (By.XPATH, '//fieldset[2]//input')  # Login: input field "Пароль"
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Login: button "Войти"

    LOCATOR_MY_ACC_LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # My account: button 'Выход'
    LOCATOR_MY_ACC_CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')  # My account: button 'Конструктор'
    LOCATOR_MY_ACC_HEADER_LOGO = (
    By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a')  # My account: header logo

    LOCATOR_FORGOT_PASSWORD_LOGIN_BUTTON = (By.XPATH, '//a[text()="Войти"]')  # Forgot password: button 'Войти'
