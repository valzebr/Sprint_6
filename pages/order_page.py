import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators



class OrderPage(BasePage):

    @allure.step('Заполнение поля Имя')
    def send_first_name(self, text):
        self.send_keys_to_place(OrderPageLocators.first_name_place, text)

    @allure.step('Заполнение поля Фамилия')
    def send_last_name(self, text):
        self.send_keys_to_place(OrderPageLocators.second_name_place, text)

    @allure.step('Заполнение поля Адрес')
    def send_address(self, text):
        self.send_keys_to_place(OrderPageLocators.address_place, text)

    @allure.step('Заполнение поля Станция метро')
    def send_metro(self, text):
        self.send_keys_to_place(OrderPageLocators.metro_place, text)

    @allure.step('Заполнение поля Номер телефона')
    def send_telephone(self, text):
        self.send_keys_to_place(OrderPageLocators.telephone_place, text)

    @allure.step('Клик на кнопку Далее')
    def click_next_button(self):
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Заполнение поля Когда привезти самокат')
    def send_date(self, text):
        self.send_keys_to_place(OrderPageLocators.when_to_bring_place, text)

    @allure.step('Заполнение поля Срок аренды')
    def send_rental_period(self, locator):
        self.send_keys_to_place(OrderPageLocators.rental_period_place, locator)

    @allure.step('Заполнение поля Цвет самоката')
    @allure.step('Заполнение поля Комментарий для курьера')
    @allure.step('Клик на кнопку Назад')
    @allure.step('Клик на кнопку Заказать')
