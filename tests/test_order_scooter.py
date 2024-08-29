import allure

from conftest import *
from multiprocessing.dummy import current_process
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from pages.home_page import HomePageHeader
from pages.order_page import *

class TestOrder:

    @allure.title('Проверка всего флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize("user_data",[Users.user_1, Users.user_2])
    def test_correct_oder(self, driver, user_data):
        home_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        home_page.first_order_button_click()
        order_page.send_first_name(user_data)
        order_page.send_last_name(user_data)
        order_page.send_address(user_data)
        order_page.send_metro(user_data)
        order_page.send_telephone(user_data)
        order_page.click_next_button()
        order_page.send_date(user_data)
        order_page.send_rental_period(user_data)
        order_page.send_color_scooter(user_data)
        order_page.send_comment(user_data)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.show_status_text()