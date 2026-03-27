"""Тестовые данные для автотестов Stellar Burgers"""

import random
import string


class TestData:
    """Класс для генерации тестовых данных"""

    @staticmethod
    def generate_random_string(length=10):
        """Генерация случайной строки"""
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_user_data():
        """Генерация данных для создания пользователя"""
        random_string = TestData.generate_random_string()
        return {
            "email": f"test_{random_string}@yandex.ru",
            "password": "password123",
            "name": f"TestUser_{random_string}",
        }

    @staticmethod
    def generate_login_data(email, password):
        """Генерация данных для логина"""
        return {"email": email, "password": password}


class Ingredients:
    """Класс с константами ингредиентов"""

    # Базовые ID ингредиентов (будут получены через API)
    BUN = None
    MAIN = None
    SAUCE = None

    # Типы ингредиентов
    TYPES = {
        "bun": "bun",
        "main": "main",
        "sauce": "sauce",
    }