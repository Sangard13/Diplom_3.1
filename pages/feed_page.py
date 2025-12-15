import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self, url):
        """Открыть страницу ленты заказов"""
        self.open(url)
        self.wait_for_page_load()

    @allure.step("Проверить, что находимся на странице ленты заказов")
    def is_on_feed_page(self):
        """Проверить, что находимся на странице ленты заказов"""
        return self.is_element_visible(FeedPageLocators.FEED_TITLE)

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_orders_counter(self):
        """
        Получить значение счётчика выполненных заказов за всё время
        :return: число заказов
        """
        counter_text = self.get_text(FeedPageLocators.TOTAL_ORDERS_COUNTER)
        # Убираем пробелы и преобразуем в число
        return int(counter_text.replace(" ", ""))

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        """
        Получить значение счётчика выполненных заказов за сегодня
        :return: число заказов
        """
        counter_text = self.get_text(FeedPageLocators.TODAY_ORDERS_COUNTER)
        # Убираем пробелы и преобразуем в число
        return int(counter_text.replace(" ", ""))

    @allure.step("Ожидать появления заказа в ленте")
    def wait_for_order_in_feed(self, order_number, timeout=10):
        """
        Ожидать появления заказа с указанным номером в ленте заказов
        """
        order_str = str(order_number)

        # Ищем номер заказа (с префиксом # или без)
        locator = (By.XPATH, f"//*[contains(@class, 'digits-default') and contains(text(), '{order_str}')]")

        return self.wait_for_element_visible(locator, timeout=timeout)

    @allure.step("Проверить наличие заказа в ленте")
    def is_order_in_feed(self, order_number):
        """
        Проверить наличие заказа в ленте
        :param order_number: номер заказа
        :return: True если заказ присутствует
        """
        order_formatted = str(order_number).zfill(7)
        template = FeedPageLocators.ORDER_NUMBER_TEMPLATE
        locator = template.format(order_formatted)
        return self.is_element_present(locator)

    @allure.step("Найти раздел 'В работе'")
    def find_progress_section(self, timeout=10):
        """Найти раздел 'В работе' на странице ленты заказов"""
        return self.find_element(FeedPageLocators.PROGRESS_SECTION, timeout=timeout)

    @allure.step("Проверить наличие заказа в разделе 'В работе'")
    def check_order_in_progress_section(self, order_number, progress_section):
        """Проверить наличие заказа в разделе 'В работе'"""
        order_str = str(order_number)

        # Получаем локатор через наследование
        locator = FeedPageLocators.get_order_in_progress_locator(order_number)

        # Ищем элементы
        elements = progress_section.find_elements(*locator)

        # Проверяем
        return bool(elements) or order_str in progress_section.text