import allure
from conftest import *
import pytest
from data import *
from pages.home_page import *
from pages.order_page import *

class TestQuestions:
    @allure.title('Тест проверки текста ответов на вопросы на главной странице веб-приложения')

    @pytest.mark.parametrize('question_locator, question_text_locator, expected_question_text', zip(BodyLocators.questions, BodyLocators.answers_text, Questions.expected_question_text))
    def test_questions(self, driver, question_locator, question_text_locator, expected_question_text):
        home_page = HomePageBody(driver)
        text = home_page.get_text_question(question_locator, question_text_locator)

        assert text == expected_question_text