from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import sys


class DriverFactory:
    """Фабрика для создания WebDriver"""

    @staticmethod
    def get_driver(browser_name):
        """Получить драйвер для указанного браузера"""
        creators = {
            'chrome': DriverFactory.create_chrome_driver,
            'firefox': DriverFactory.create_firefox_driver,
        }

        driver_creator = creators.get(browser_name.lower())
        if not driver_creator:
            raise ValueError(f"Браузер {browser_name} не поддерживается")

        return driver_creator()

    @staticmethod
    def create_chrome_driver():
        """Создание Chrome драйвера с настройками"""
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")

        try:
            # Пробуем скачать драйвер через менеджер
            driver_path = ChromeDriverManager().install()
            print(f"Путь к драйверу от менеджера: {driver_path}")

            # Исправляем путь - ищем chromedriver.exe
            if not driver_path.endswith('.exe'):
                driver_dir = os.path.dirname(driver_path)

                # Ищем chromedriver.exe в директории
                chromedriver_exe = None
                for file in os.listdir(driver_dir):
                    if 'chromedriver' in file.lower() and file.endswith('.exe'):
                        chromedriver_exe = os.path.join(driver_dir, file)
                        break

                if chromedriver_exe:
                    driver_path = chromedriver_exe
                    print(f"Найден chromedriver.exe: {driver_path}")
                else:
                    # Ищем рекурсивно
                    for root, dirs, files in os.walk(driver_dir):
                        for file in files:
                            if 'chromedriver' in file.lower() and file.endswith('.exe'):
                                driver_path = os.path.join(root, file)
                                print(f"Найден chromedriver.exe в подпапке: {driver_path}")
                                break
                        if driver_path.endswith('.exe'):
                            break

            # Создаем драйвер
            driver = webdriver.Chrome(
                service=ChromeService(driver_path),
                options=options,
            )

        except Exception as e:
            print(f"Ошибка при создании драйвера: {e}")

            # Пробуем альтернативный метод
            try:
                # Создаем драйвер без указания пути (если chromedriver в PATH)
                driver = webdriver.Chrome(options=options)
            except:
                # Последняя попытка - ручной путь
                print("Пробуем ручной путь к драйверу...")
                manual_path = r"C:\chromedriver.exe"
                if os.path.exists(manual_path):
                    driver = webdriver.Chrome(
                        service=ChromeService(manual_path),
                        options=options,
                    )
                else:
                    # Создаем простой драйвер без service
                    driver = webdriver.Chrome(options=options)

        return driver

    @staticmethod
    def create_firefox_driver():
        """Создание Firefox драйвера с настройками"""
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )

        return driver
