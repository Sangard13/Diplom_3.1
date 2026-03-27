import pytest
import allure
from driver_factory import DriverFactory
from helpers.api_helpers import StellarBurgersAPI
from data import TestData


def pytest_addoption(parser):
    """Добавление опции командной строки для выбора браузера"""
    parser.addoption(
        "--browser-name",
        action="store",
        default="chrome",
        help="Выбор браузера: chrome или firefox",
    )


@pytest.fixture(scope="function")
def browser_name(request):
    """Фикстура для получения имени браузера из командной строки"""
    return request.config.getoption("--browser-name")


@pytest.fixture(scope="function")
def driver(request, browser_name):
    """Фикстура для создания и закрытия WebDriver"""
    # Добавляем информацию о браузере в Allure отчёт
    allure.dynamic.parameter("Browser", browser_name.upper())

    # Создаем драйвер через фабрику
    driver = DriverFactory.get_driver(browser_name)

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    # Сделать скриншот при падении теста
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

    driver.quit()


@pytest.fixture(scope="function")
def user_with_order():
    """
    Фикстура создания пользователя и заказа через API
    :return: данные пользователя и API клиент
    """
    api = StellarBurgersAPI()

    # Генерируем данные пользователя
    user_data = TestData.generate_user_data()

    # Создаём пользователя
    response = api.create_user(user_data)
    assert (
            response.status_code == 200
    ), f"Не удалось создать пользователя: {response.text}"

    # Получаем токен
    access_token = response.json().get("accessToken")

    yield {"user_data": user_data, "api": api, "token": access_token}

    # Удаляем пользователя после теста
    if access_token:
        api.delete_user(access_token)


@pytest.fixture(scope="function")
def logged_in_user(driver, user_with_order):
    """
    Фикстура для авторизованного пользователя
    :return: данные пользователя
    """
    # Импортируем здесь, чтобы избежать циклических импортов
    from pages.login_page import LoginPage

    login_page = LoginPage(driver)
    user_data = user_with_order["user_data"]

    # Логинимся через UI
    login_page.open_login_page()
    login_page.login(user_data["email"], user_data["password"])

    return user_with_order


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для сохранения результата выполнения теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function")
def drag_and_drop_js():
    """
    JavaScript функция для drag-and-drop.
    Необходима для корректной работы в Firefox.
    """
    return """
    function simulateDragDrop(sourceNode, destinationNode) {
        var EVENT_TYPES = {
            DRAG_END: 'dragend',
            DRAG_START: 'dragstart',
            DROP: 'drop'
        }

        function createCustomEvent(type) {
            var event = new CustomEvent("CustomEvent")
            event.initCustomEvent(type, true, true, null)
            event.dataTransfer = {
                data: {
                },
                setData: function(type, val) {
                    this.data[type] = val
                },
                getData: function(type) {
                    return this.data[type]
                }
            }
            return event
        }

        function dispatchEvent(node, type, event) {
            if (node.dispatchEvent) {
                return node.dispatchEvent(event)
            }
            if (node.fireEvent) {
                return node.fireEvent("on" + type, event)
            }
        }

        var event = createCustomEvent(EVENT_TYPES.DRAG_START)
        dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event)

        var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
        dropEvent.dataTransfer = event.dataTransfer
        dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)

        var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
        dragEndEvent.dataTransfer = event.dataTransfer
        dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
    }

    simulateDragDrop(arguments[0], arguments[1]);
    """