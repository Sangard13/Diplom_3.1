"""Page Object для модального окна ингредиента"""

import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModal(BasePage):
    """Класс для работы с модальным окном деталей ингредиента"""

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        """Проверить, что модальное окно открыто"""
        return self.is_element_visible(IngredientModalLocators.MODAL)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Проверить, что модальное окно закрыто"""
        return self.wait_for_element_to_disappear(IngredientModalLocators.MODAL)

    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        """Получить текст заголовка модального окна"""
        return self.get_text(IngredientModalLocators.MODAL_TITLE)

    @allure.step("Получить название ингредиента")
    def get_ingredient_name(self):
        """Получить название ингредиента из модального окна"""
        return self.get_text(IngredientModalLocators.INGREDIENT_NAME)

    @allure.step("Кликнуть на кнопку закрытия (крестик)")
    def click_close_button(self):
        """Закрыть модальное окно кликом по крестику"""
        self.click_element(IngredientModalLocators.CLOSE_BUTTON)

    @allure.step("Проверить наличие изображения ингредиента")
    def is_ingredient_image_visible(self):
        """Проверить, отображается ли изображение ингредиента"""
        return self.is_element_visible(IngredientModalLocators.INGREDIENT_IMAGE)