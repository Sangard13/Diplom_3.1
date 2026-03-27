"""Локаторы для страницы ленты заказов"""

from selenium.webdriver.common.by import By


class FeedPageLocators:
    """Локаторы элементов страницы ленты заказов"""

    # Заголовок страницы
    FEED_TITLE = (
        By.XPATH,
        "//h1[text()='Лента заказов']",
    )

    # Счётчики
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )

    # Номер заказа в списке заказов
    ORDER_NUMBER_TEMPLATE = "//p[text()='#{}']"

    # Для страницы ленты заказов
    PROGRESS_SECTION = (By.XPATH, "//section[.//h2[contains(text(), 'В работе')]]")
    PROGRESS_SECTION_ALT = (By.XPATH, "//div[.//h2[contains(text(), 'В работе')]]")

    @staticmethod
    def get_order_in_progress_locator(order_number):
        """Получить локатор для поиска заказа в разделе 'В работе'"""
        order_str = str(order_number)
        return (By.XPATH, f".//*[contains(text(), '{order_str}') or contains(text(), '#{order_str}')]")