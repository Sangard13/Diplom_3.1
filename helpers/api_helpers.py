"""API хелперы для работы с Stellar Burgers API"""

import requests
import allure
from urls import API_ENDPOINTS


class StellarBurgersAPI:
    """Класс для работы с API Stellar Burgers"""

    def __init__(self):
        self.base_url = API_ENDPOINTS

    @allure.step("API: Создать пользователя")
    def create_user(self, user_data):
        """
        Создание пользователя через API
        :param user_data: dict с полями email, password, name
        :return: response object
        """
        response = requests.post(self.base_url["register"], json=user_data)
        return response

    @allure.step("API: Авторизовать пользователя")
    def login_user(self, login_data):
        """
        Авторизация пользователя через API
        :param login_data: dict с полями email, password
        :return: response object
        """
        response = requests.post(self.base_url["login"], json=login_data)
        return response

    @allure.step("API: Удалить пользователя")
    def delete_user(self, access_token):
        """
        Удаление пользователя через API
        :param access_token: токен авторизации
        :return: response object
        """
        headers = {"Authorization": access_token}
        response = requests.delete(self.base_url["user"], headers=headers)
        return response

    @allure.step("API: Создать заказ")
    def create_order(self, ingredients, access_token=None):
        """
        Создание заказа через API
        :param ingredients: список ID ингредиентов
        :param access_token: токен авторизации (опционально)
        :return: response object
        """
        headers = {}
        if access_token:
            headers["Authorization"] = access_token

        data = {"ingredients": ingredients}
        response = requests.post(self.base_url["orders"], json=data, headers=headers)
        return response

    @allure.step("API: Получить список ингредиентов")
    def get_ingredients(self):
        """
        Получение списка всех ингредиентов через API
        :return: response object
        """
        response = requests.get(self.base_url["ingredients"])
        return response

    @allure.step("API: Получить ID ингредиентов по типу")
    def get_ingredient_ids_by_type(self, ingredient_type, count=1):
        """
        Получить ID ингредиентов по типу
        :param ingredient_type: тип ингредиента (bun, main, sauce)
        :param count: количество ингредиентов
        :return: список ID ингредиентов
        """
        response = self.get_ingredients()
        if response.status_code == 200:
            ingredients = response.json().get("data", [])
            filtered = [
                ing["_id"] for ing in ingredients if ing["type"] == ingredient_type
            ]
            return filtered[:count]
        return []

    @allure.step("API: Создать заказ со случайными ингредиентами")
    def create_order_with_random_ingredients(self, access_token):
        """
        Создать заказ со случайными ингредиентами
        :param access_token: токен авторизации
        :return: response object
        """
        # Получаем по одному ингредиенту каждого типа
        bun = self.get_ingredient_ids_by_type("bun", 1)
        main = self.get_ingredient_ids_by_type("main", 1)
        sauce = self.get_ingredient_ids_by_type("sauce", 1)

        # Формируем список ингредиентов для заказа
        ingredients = bun + main + sauce

        # Создаем заказ
        return self.create_order(ingredients, access_token)