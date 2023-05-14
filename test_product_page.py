from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
        email,password = page.generate_email_and_pass()
        page.register_new_user(email,password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.should_not_be_success_message()

    #@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail(reason="some bug")),
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        #page.should_be_login_link()
        page.open()
        page.should_be_product_page_url()   # проверяем что находимся на страеице продукта
        page.should_cart_button()           # Проверяем что кнопка доступна
        #page.should_not_be_success_message() #Проверяем что сообщения о добавление товара нет. - очень осторожная проверка https://habr.com/ru/company/badoo/blog/419419/
                                              #Обязательно проверяем позже что такой эллемент есть на странице. т.е ссылка можеи поменяться и дать положительный результат.
        expected_price = page.save_amount_of_good_with_current_cart()          #Сохраняем значения суммы корзины
        name_of_product = page.save_name_of_product()        #Сохраняем название товара
        page.click_to_cart_button()         # Кликаем по кнопке
        page.solve_quiz_and_get_code()      # Обрабатываем всплывающие окно
        page.expected_result_good_in_cart_add_notify_same(name_of_product) #Ожидаемый результат товар который добавили == добавился с правильным названием в карзину.
        page.expected_result_good_price_add_notify_same(expected_price) #ПРоверяем что товар по стоимость добавился в корзину
        #page.should_be_success_message_disappeared() # Проверяем что сообщение о добавленном товаре исчезло

@pytest.mark.check_empty_bascet_productpage
@pytest.mark.skip
class TestShoudEmptyBasketFromProductPage():
#Перед отрицательной проверкой проверяем что такая ссылка есть
    def test_guest_add_good_in_basket_and_check_patch(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.click_to_cart_button()
        page.should_be_basket_link()
        page.going_to_busket()
        basket_page = BasketPage(browser,browser.current_url)
        basket_page.expected_result_product_in_busket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_link()
        page.going_to_busket()
        basket_page = BasketPage(browser,browser.current_url)
        basket_page.should_be_basket_url()
        basket_page.expected_result_not_product_in_busket() #проверяем что нет товаров в корзине
        basket_page.expected_result_not_product_in_busket_notify() #проверяем корзина пустая

@pytest.mark.login_guest_from_productpage
@pytest.mark.skip
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем  страницу
    page.click_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем  страницу
    page.click_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_disappeared()
