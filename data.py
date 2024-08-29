from locators.main_page_locators import HeaderLocators, BodyLocators
from locators.order_page_locators import *

class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'
    ORDER_URL = 'https://qa-scooter.praktikum-services.ru/order'


class Users:
    user_1 = {
        'button': HeaderLocators.order_button_1,
        'first_name': 'Андрей',
        'last_name': 'Петров',
        'address': 'Москва, ул. Льва Толстого, д. 16',
        'metro': 'Преображенская площадь',
        'telephone': '89000000001',
        'calendar': '29.08.2024',
        'rental': OrderPageLocators.five_day_rental,
        'color': OrderPageLocators.black_color_checkbox,
        'comment': 'Комментарий user_1'
    }

    user_2 = {
        'button': BodyLocators.order_button_2,
        'first_name': 'Петр',
        'last_name': 'Андреев',
        'address': 'Москва, ул. Арбат, д. 26',
        'metro': 'Преображенская площадь',
        'telephone': '89000000002',
        'calendar': '30.08.2024',
        'rental': OrderPageLocators.one_day_rental,
        'color': OrderPageLocators.grey_color_checkbox,
        'comment': 'Комментарий user_1'
    }

class Questions:
    expected_question_text = [
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ]



