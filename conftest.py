from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1024, 1080)
    yield driver
    driver.quit()