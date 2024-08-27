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
