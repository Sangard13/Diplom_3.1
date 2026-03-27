from selenium.webdriver.common.by import By


class LoginLocators:
    """Локаторы элементов страницы авторизации"""

    # Поля ввода
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input"
    )

    # Кнопки и ссылки
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[text()='Восстановить пароль']"
    )

    REGISTER_LINK = (
        By.XPATH,
        "//a[text()='Зарегистрироваться']"
    )

    # Заголовок страницы
    LOGIN_TITLE = (
        By.XPATH,
        "//h2[text()='Вход']"
    )