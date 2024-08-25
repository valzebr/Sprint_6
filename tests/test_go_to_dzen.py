from multiprocessing.dummy import current_process
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from pages.base_page import BasePage

class TestDzen:

    def test_clik_yandex_button_go_to_dzen(self, driver):
        BasePage.get_url(Urls.BASE_URL)

        # Ждем, пока откроется новая вкладка
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Переключаемся на новую вкладку
        for window in driver.window_handles:
            if window != Urls.DZEN_URL:
                driver.switch_to.window(window)
                break

        # Проверяем URL новой вкладки
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.DZEN_URL))
        assert driver.current_url == Urls.DZEN_URL