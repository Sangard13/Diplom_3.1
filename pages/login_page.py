import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from urls import PAGES


class LoginPage(BasePage):
    """Класс для работы со страницей авторизации"""

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        """Открыть страницу авторизации"""
        self.open(PAGES["login"])
        self.wait_for_page_load()

    @allure.step("Авторизоваться с email: {email}")
    def login(self, email, password):
        """
        Авторизация пользователя
        :param email: email пользователя
        :param password: пароль пользователя
        """
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()

    @allure.step("Ввести email: {email}")
    def input_email(self, email):
        """Ввести email в поле ввода"""
        self.input_text(LoginLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def input_password(self, password):
        """Ввести пароль в поле ввода"""
        self.input_text(LoginLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_login_button(self):
        """Кликнуть на кнопку входа"""
        self.click_element(LoginLocators.LOGIN_BUTTON)

    @allure.step("Проверить, что находимся на странице авторизации")
    def is_on_login_page(self):
        """Проверить, что находимся на странице авторизации"""
        return self.is_element_visible(LoginLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        """Кликнуть на ссылку восстановления пароля"""
        self.click_element(LoginLocators.FORGOT_PASSWORD_LINK)