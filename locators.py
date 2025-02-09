from selenium.webdriver.common.by import By


class Locators:
    locator_reg_name = (By.XPATH, '//fieldset[1]//input')  # Registration: input field "Имя"
    locator_reg_email = (By.XPATH, '//fieldset[2]//input')  # Registration: input field "Email"
    locator_reg_password = (By.XPATH, '//fieldset[3]//input[@name="Пароль"]')  # Registration: input field "Пароль"
    locator_reg_button = (
    By.XPATH, '//button[text()="Зарегистрироваться"]')  # Registration: button "Зарегистрироваться"
    locator_reg_password_error = (
    By.XPATH, '//p[text()="Некорректный пароль"]')  # Registration: password validation error
    locator_reg_login_button = (By.XPATH, '//a[text()="Войти"]')  # Registration: button 'Войти'

    locator_main_goto_acc_button = (
    By.XPATH, '//button[text()="Войти в аккаунт"]')  # Main page: button "Войти в аккаунт"
    locator_main_make_order = (
    By.XPATH, '//button[text()="Оформить заказ"]')  # Main page, logged-in user: button "Оформить заказ"
    locator_main_my_account = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Main page: button "Личный Кабинет"

    locator_main_buns_section = (By.XPATH, '//span[text()="Булки"]')  # Main page: section "Булки"
    locator_main_buns_check_selected_state = (
    By.XPATH, '//span[text()="Булки"]/parent::div')  # Main page: section "Булки" -> parent div
    locator_main_sauces_section = (By.XPATH, '//span[text()="Соусы"]')  # Main page: section "Соусы"
    locator_main_sauces_check_selected_state = (
    By.XPATH, '//span[text()="Соусы"]/parent::div')  # Main page: section "Соусы" -> parent div
    locator_main_filings_section = (By.XPATH, '//span[text()="Начинки"]')  # Main page: section "Начинки"
    locator_main_filings_check_selected_state = (
    By.XPATH, '//span[text()="Начинки"]/parent::div')  # Main page: section "Начинки" -> parent div

    locator_login_email = (By.XPATH, '//fieldset[1]//input')  # Login: input field "Email"
    locator_login_password = (By.XPATH, '//fieldset[2]//input')  # Login: input field "Пароль"
    locator_login_button = (By.XPATH, '//button[text()="Войти"]')  # Login: button "Войти"

    locator_my_acc_logout_button = (By.XPATH, '//button[text()="Выход"]')  # My account: button 'Выход'
    locator_my_acc_constructor_button = (By.XPATH, '//p[text()="Конструктор"]')  # My account: button 'Конструктор'
    locator_my_acc_header_logo = (
    By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a')  # My account: header logo

    locator_forgot_password_login_button = (By.XPATH, '//a[text()="Войти"]')  # Forgot password: button 'Войти'
