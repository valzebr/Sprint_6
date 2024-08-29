from selenium import webdriver
import pytest
import allure
from data import Urls

@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    driver.set_window_size(1024, 1080)
    yield driver
    driver.quit()

# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    return repr(val)