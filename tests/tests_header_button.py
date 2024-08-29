import time
from multiprocessing.dummy import current_process
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from pages.home_page import HomePageHeader
from conftest import *


class TestHeaderButton:

    @allure.title('Проверка если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_correct_go_to_scooter_button(self, driver):
        home_page = HomePageHeader(driver)
        correct_url = Urls.BASE_URL
        home_page.first_order_button_click()
        home_page.scooter_logo_click()
        assert correct_url == Urls.BASE_URL

    @allure.title('Проверка если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_click_yandex_go_to_dzen(self, driver):
        home_page = HomePageHeader(driver)
        correct_url = Urls.DZEN_URL
        home_page.yandex_button_click()
        home_page.go_to_new_tab()
        time.sleep(2)
        assert driver.current_url == correct_url