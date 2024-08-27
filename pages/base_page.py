from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Получить текущий URL
    def get_url(self):
        return self.driver.url

    # Ожидание отображения локатора
    def find_and_wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # Клик по кнопке
    def click_button(self, locator):
        self.find_and_wait_element(locator).click()

    # Заполнение формы
    def send_keys_to_place(self,locator,text):
        self.find_and_wait_element(locator).send_keys(text)

    # Получить текст элемента
    def get_text_locator(self, locator):
        return self.find_and_wait_element(locator).text

    # Скролл к нужному элементу
    def scroll_to_element(self, locator):
        element = self.find_and_wait_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    # Переход на новую вкладку браузера
    def change_modal(self, locator):
        modal = self.find_and_wait_element(locator)
        self.driver.switch_to.frame(modal)
