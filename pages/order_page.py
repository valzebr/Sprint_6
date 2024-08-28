import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators



class OrderPage(BasePage):

    @allure.step('Заполнение поля Имя')
    def send_first_name(self, user_data):
        self.send_keys_to_place(OrderPageLocators.first_name_place, user_data['first_name'])

    @allure.step('Заполнение поля Фамилия')
    def send_last_name(self, user_data):
        self.send_keys_to_place(OrderPageLocators.second_name_place, user_data['last_name'])

    @allure.step('Заполнение поля Адрес')
    def send_address(self, user_data):
        self.send_keys_to_place(OrderPageLocators.address_place, user_data['address'])

    @allure.step('Заполнение поля Станция метро')
    def send_metro(self, user_data):
        self.click_button(OrderPageLocators.metro_place)
        self.send_keys_to_place(OrderPageLocators.metro_place, user_data['metro'])
        self.click_button(OrderPageLocators.metro_wtf)


    @allure.step('Заполнение поля Номер телефона')
    def send_telephone(self, user_data):
        self.send_keys_to_place(OrderPageLocators.telephone_place, user_data['telephone'])

    @allure.step('Клик на кнопку Далее')
    def click_next_button(self):
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Заполнение поля Когда привезти самокат')
    def send_date(self, user_data):
        self.click_button(OrderPageLocators.when_to_bring_place)
        self.send_keys_to_place(OrderPageLocators.when_to_bring_place, user_data['calendar'])

    @allure.step('Заполнение поля Срок аренды')
    def send_rental_period(self, user_data):
        self.click_button(OrderPageLocators.rental_period_place)
        self.click_button(user_data['rental'])

    @allure.step('Заполнение поля Цвет самоката')
    def send_color_scooter(self, user_data):
        self.click_button(user_data['color'])

    @allure.step('Заполнение поля Комментарий для курьера')
    def send_comment(self, user_data):
        self.send_keys_to_place(OrderPageLocators.when_to_bring_place, user_data['comment'])

    @allure.step('Клик на кнопку Назад')
    def click_backspace_button(self):
        self.click_button(OrderPageLocators.backspace_button)

    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self):
        self.click_button(OrderPageLocators.order_button)

    @allure.step('Клик на кнопку подтверждения заказа')
    def click_yes_button(self):
        self.click_button(OrderPageLocators.yes_button)

    @allure.step('Клик на кнопку отмены заказа')
    def click_no_button(self):
        self.click_button(OrderPageLocators.no_button)

    @allure.step('Окно Заказ оформлен')
    def show_status_text(self):
        return self.find_and_wait_element(OrderPageLocators.show_status_text).is_displayed()