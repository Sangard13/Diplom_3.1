import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.ingredient_modal import IngredientModal
from urls import PAGES, URL_PARTS


@allure.feature("Основная функциональность")
@allure.story("Навигация и взаимодействие с элементами")
class TestMainFunctionality:
    """Тесты основной функциональности приложения"""

    @allure.title("Переход по клику на 'Конструктор'")
    @allure.description(
        "Проверка перехода на главную страницу при клике на 'Конструктор'"
    )
    def test_navigate_to_constructor(self, driver):
        """
        Тест проверяет переход на главную страницу (конструктор)
        1. Открываем главную страницу
        2. Переходим на страницу ленты заказов
        3. Кликаем на кнопку 'Конструктор'
        4. Проверяем, что вернулись на главную страницу
        """
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        # Открываем главную страницу
        main_page.open_main_page(PAGES["main"])

        # Переходим на страницу ленты заказов
        main_page.click_feed_button()
        assert feed_page.is_on_feed_page(), "Не удалось перейти на ленту заказов"

        # Кликаем на кнопку Конструктор
        main_page.click_constructor_button()

        # Проверяем, что вернулись на главную страницу
        assert main_page.wait_for_url_contains(
            URL_PARTS["domain"]
        ), f"URL не содержит '{URL_PARTS['domain']}'"
        assert main_page.is_on_main_page(), (
            "Не удалось вернуться на главную страницу " "после клика на 'Конструктор'"
        )

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    @allure.description(
        "Проверка перехода на страницу ленты заказов при клике на кнопку"
    )
    def test_navigate_to_feed(self, driver):
        """
        Тест проверяет переход на страницу ленты заказов
        1. Открываем главную страницу
        2. Кликаем на кнопку 'Лента Заказов'
        3. Проверяем, что перешли на страницу ленты заказов
        """
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        # Открываем главную страницу
        main_page.open_main_page(PAGES["main"])

        # Кликаем на кнопку Лента Заказов
        main_page.click_feed_button()

        # Проверяем, что перешли на страницу ленты заказов
        assert feed_page.wait_for_url_contains(
            URL_PARTS["feed"]
        ), f"URL не содержит '{URL_PARTS['feed']}'"
        assert (
            feed_page.is_on_feed_page()
        ), "Не удалось перейти на страницу ленты заказов"

    @allure.title("Открытие модального окна при клике на ингредиент")
    @allure.description("Проверка открытия модального окна с деталями ингредиента")
    def test_ingredient_modal_opens(self, driver):
        """
        Тест проверяет открытие модального окна при клике на ингредиент
        1. Открываем главную страницу
        2. Кликаем на ингредиент
        3. Проверяем, что модальное окно открылось
        4. Проверяем наличие всех элементов модального окна
        """
        main_page = MainPage(driver)
        modal = IngredientModal(driver)

        # Открываем главную страницу
        main_page.open_main_page(PAGES["main"])

        # Кликаем на первый ингредиент
        main_page.click_first_ingredient()

        # Проверяем, что модальное окно открылось
        assert (
            modal.is_modal_opened()
        ), "Модальное окно не открылось после клика на ингредиент"

        # Проверяем заголовок
        assert (
            modal.get_modal_title() == "Детали ингредиента"
        ), "Заголовок модального окна не соответствует ожидаемому"

        # Проверяем наличие названия ингредиента
        ingredient_name = modal.get_ingredient_name()
        assert ingredient_name, "Название ингредиента не отображается в модальном окне"

        # Проверяем наличие изображения
        assert (
            modal.is_ingredient_image_visible()
        ), "Изображение ингредиента не отображается"

    @allure.title("Закрытие модального окна по крестику")
    @allure.description(
        "Проверка закрытия модального окна при клике на кнопку закрытия"
    )
    def test_ingredient_modal_closes(self, driver):
        """
        Тест проверяет закрытие модального окна при клике на крестик
        1. Открываем главную страницу
        2. Кликаем на ингредиент для открытия модального окна
        3. Кликаем на крестик для закрытия
        4. Проверяем, что модальное окно закрылось
        """
        main_page = MainPage(driver)
        modal = IngredientModal(driver)

        # Открываем главную страницу
        main_page.open_main_page(PAGES["main"])

        # Открываем модальное окно
        main_page.click_first_ingredient()
        assert modal.is_modal_opened(), "Модальное окно не открылось"

        # Закрываем модальное окно кликом по крестику
        modal.click_close_button()

        # Проверяем, что модальное окно закрылось
        assert (
            modal.is_modal_closed()
        ), "Модальное окно не закрылось после клика на крестик"

    @allure.title("Увеличение счётчика при добавлении ингредиента")
    @allure.description(
        "Проверка увеличения счётчика ингредиента " "при добавлении его в заказ"
    )
    def test_ingredient_counter_increases(self, driver):
        """
        Тест проверяет увеличение счётчика при добавлении ингредиента
        1. Открываем главную страницу
        2. Проверяем, что счётчик отсутствует (0)
        3. Перетаскиваем ингредиент в конструктор
        4. Проверяем, что счётчик показывает правильное значение
        """
        main_page = MainPage(driver)

        # Открываем главную страницу
        main_page.open_main_page(PAGES["main"])

        # Проверяем, что изначально счётчик отсутствует или равен 0
        initial_counter = main_page.get_first_ingredient_counter()
        assert (
                initial_counter == 0
        ), f"Начальный счётчик должен быть 0, получено: {initial_counter}"

        # Перетаскиваем ингредиент в конструктор
        main_page.drag_ingredient_to_constructor()

        # Ожидаем, что счётчик примет значение "2" (для булки)
        # Метод бросит исключение если таймаут, тест упадёт автоматически
        main_page.wait_for_counter_value("2", timeout=10)

        # Проверяем, что счётчик отображается
        assert (
            main_page.is_ingredient_counter_visible()
        ), "Счётчик ингредиента не отображается после добавления"

        # Получаем текст счётчика для финальной проверки
        counter_text = main_page.get_first_ingredient_counter_text()

        # Для булок счётчик увеличивается на 2 (верх и низ бургера)
        assert counter_text == "2", (
            f"Счётчик должен показывать '2' для булки, " f"получено: '{counter_text}'"
        )