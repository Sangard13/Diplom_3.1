"""Локаторы для модального окна ингредиента"""

from selenium.webdriver.common.by import By


class IngredientModalLocators:
    """Локаторы элементов модального окна с деталями ингредиента"""

    # Модальное окно
    MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]",
    )

    # Заголовок "Детали ингредиента"
    MODAL_TITLE = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']",
    )

    # Название ингредиента в модальном окне
    INGREDIENT_NAME = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']/following-sibling::p",
    )

    # Изображение ингредиента
    INGREDIENT_IMAGE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]//img",
    )

    # Кнопка закрытия (крестик)
    CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "section[class*='Modal_modal'] button[class*='close']",
    )