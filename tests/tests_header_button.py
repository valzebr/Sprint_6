import time
from multiprocessing.dummy import current_process
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from pages import dzen_page
from pages.home_page import *
from pages.dzen_page import *
from pages.base_page import *
from conftest import *


class TestHeaderButton:

    @allure.title('Проверка если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_correct_go_to_scooter_button(self, driver):
        home_page = HomePageHeader(driver)
        home_page.first_order_button_click()
        home_page.scooter_logo_click()
        current_url = home_page.get_url()
        title_is_displayed = home_page.check_order_title()
        assert current_url == Urls.BASE_URL and title_is_displayed





    @allure.title('Проверка если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_click_yandex_go_to_dzen(self, driver):
        home_page = HomePageHeader(driver)
        dzen_page = DzenPage(driver)
        current_url = Urls.DZEN_URL
        home_page.yandex_button_click()
        home_page.go_to_new_tab(Urls.DZEN_URL)
        assert current_url == Urls.DZEN_URL and dzen_page.check_element_main_button()