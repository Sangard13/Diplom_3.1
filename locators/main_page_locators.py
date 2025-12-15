from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов главной страницы"""

    # Навигация в шапке
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//a[@href='/' and contains(@class, 'AppHeader')]//p[text()='Конструктор']",
    )
    FEED_BUTTON = (
        By.XPATH,
        "//a[@href='/feed']//p[text()='Лента Заказов']",
    )

    # Секции конструктора (табы)
    BUN_TAB = (
        By.XPATH,
        "//span[text()='Булки']",
    )

    # Ингредиенты
    FIRST_BUN = (
        By.XPATH,
        "(//section[.//h2[text()='Булки']]//a[contains(@class, 'BurgerIngredient')])[1]",
    )
    FIRST_SAUCE = (
        By.XPATH,
        "(//section[.//h2[text()='Соусы']]//a[contains(@class, 'BurgerIngredient')])[1]",
    )
    FIRST_MAIN = (
        By.XPATH,
        "(//section[.//h2[text()='Начинки']]//a[contains(@class, 'BurgerIngredient')])[1]",
    )

    # Счётчики ингредиентов
    FIRST_INGREDIENT_COUNTER = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient')])[1]//p[contains(@class, 'counter_counter__num')]",
    )

    # Область конструктора (для перетаскивания)
    DROP_TARGET = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor')]",
    )

    # Кнопка создания заказа
    CREATE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Оформить заказ')]",
    )

    # Модальное окно заказа
    ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal')]//p[contains(text(), 'идентификатор заказа')]",
    )

    # Номер заказа в модальном окне
    ORDER_NUMBER = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal')]//p[contains(@class, 'digits-large')]",
    )

    # Кнопка закрытия модального окна заказа
    CLOSE_ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal')]//button[contains(@class, 'close')]",
    )

    # Локаторы для авторизации
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти в аккаунт')]",
    )

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@name='name' and @type='text']",
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@name='Пароль' and @type='password']",
    )

    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти')]",
    )

    # Локатор для проверки успешной авторизации (кнопка "Оформить заказ" видна)
    AUTH_SUCCESS_INDICATOR = (
        By.XPATH,
        "//button[contains(text(), 'Оформить заказ')]",
    )