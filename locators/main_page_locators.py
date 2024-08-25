from selenium.webdriver.common.by import By


class HeaderLocators:
    """Хедер"""
    yandex_logo = (By.CSS_SELECTOR, "[class*='Header_LogoYandex']")
    scooter_logo = (By.CSS_SELECTOR, "[class*='Header_LogoScooter']")
    order_button_1 = (By.XPATH, "(//button[contains(@class, 'Button_') and text()='Заказать'])[1]")
    status_button = (By.CSS_SELECTOR, "[class*='Header_Link_']")

class BodyLocators:
    """Тело"""
    order_button_2 = (By.XPATH, "(//button[contains(@class, 'Button_') and text()='Заказать'])[2]")
    cooke_button = (By.ID, 'rcc-confirm-button')
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")

    """Вопросы о важном"""
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    """Ответы"""
    answers_text = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]
