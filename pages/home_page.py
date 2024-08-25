import allure
from locators.main_page_locators import BodyLocators, HeaderLocators
from pages.base_page import BasePage



class HomePageHeader(BasePage):


    @allure.step('Лого Яндекса')
    def yandex_button_click(self):
        self.click_button(HeaderLocators.yandex_logo)

    @allure.step('Лого Самокат')
    def scooter_logo_click(self):
        self.click_button(HeaderLocators.scooter_logo)

    @allure.step('Верхняя кнопка "Заказать"')
    def first_order_button_click(self):
        self.click_button(HeaderLocators.order_button_1)



class HomePageBody(BasePage):

    @allure.step('Скролл и клик до нижней кнопки Заказать')
    def second_order_button_click(self):
        self.scroll_to_element(BodyLocators.order_button_2)
        self.click_button(BodyLocators.order_button_2)

    @allure.step('Переход к списку вопросов')
    def scroll_to_questions_place(self):
        self.scroll_to_element(BodyLocators.questions_title)


    @allure.step('Клик на вопрос')
    def click_question_button(self, question_button_locator):
        self.scroll_to_questions_place()
        self.click_button(question_button_locator)

    @allure.step('Получение текста вопроса')
    def get_text_question(self, question_button_locator, question_text_locator):
        self.click_question_button(question_button_locator)
        text_question = self.get_text_locator(question_text_locator)
        return text_question

