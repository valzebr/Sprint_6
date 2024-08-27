from conftest import *
from multiprocessing.dummy import current_process
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from pages.base_page import BasePage
from pages.home_page import HomePageHeader
from pages.order_page import *
from locators.order_page_locators import *
import time

class TestOrderPage:

    def test_correct_oder_var1(self, driver):
        home_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        home_page.first_order_button_click()
        order_page.send_first_name(Users.user_1)
        order_page.send_last_name(Users.user_1)
        order_page.send_address(Users.user_1)
        order_page.send_metro(Users.user_1)
        order_page.send_telephone(Users.user_1)
        order_page.click_next_button()
        order_page.send_date(Users.user_1)
        order_page.send_rental_period(Users.user_1)
        order_page.send_color_scooter(Users.user_1)
        order_page.send_comment(Users.user_1)
        order_page.click_order_button(Users.user_1)
        time.sleep(1)



