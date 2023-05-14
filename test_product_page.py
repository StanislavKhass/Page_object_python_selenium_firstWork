from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

Login_and_reg_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
regular_good_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = Login_and_reg_link
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
        email,password = page.generate_email_and_pass()
        page.register_new_user(email,password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self,browser):
        link = promo_link
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = promo_link
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page_url()                                   # проверяем что находимся на страеице продукта
        page.should_cart_button()                                            # Проверяем что кнопка доступна
        page.check_locators_save_amount_of_good_with_current_cart()          #проверяем локаторы на наличие перед сохранением ожидаемой суммы
        expected_price = page.save_amount_of_good_with_current_cart()        #Сохраняем значения суммы корзины
        page.check_locators_save_name_of_product()                           #проверяем локатор на наличие перед сохранением названия
        name_of_product = page.save_name_of_product()                       #Сохраняем название товара
        page.click_to_cart_button()                                         # Кликаем по кнопке
        page.solve_quiz_and_get_code()                                     # Обрабатываем всплывающие окно
        page.check_locators_expected_result_good_in_cart_add_notify_same() # Проверяем наличие локатора названия товара перед проверкой
        page.expected_result_good_in_cart_add_notify_same(name_of_product) #Ожидаемый результат товар который добавили == добавился с правильным названием в карзину.
        page.check_locators_expected_result_good_price_add_notify_same()   # Проверяем наличие локатора высалывающей суммы перед проверкой
        page.expected_result_good_price_add_notify_same(expected_price)    #ПРоверяем что товар по стоимость добавился в корзину

#Проверяем что товара нет в корзине
#1.проверяем состояние что товар есть в корзине - test_guest_add_good_in_basket_and_check_patch
#2.проверяем что корзина пустая переходя со страницы товра - test_guest_cant_see_product_in_basket_opened_from_product_page
@pytest.mark.check_empty_bascet_productpage
class TestShoudEmptyBasketFromProductPage():
#Перед отрицательной проверкой проверяем что такая ссылка есть
    def test_guest_add_good_in_basket_and_check_patch(self,browser):
        link = regular_good_link
        page = ProductPage(browser, link)
        page.open()
        page.should_cart_button()
        page.click_to_cart_button()
        page.should_be_basket_link()
        page.going_to_busket()
        basket_page = BasketPage(browser,browser.current_url)
        basket_page.expected_result_product_in_busket()
    #отрицательная проверка
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        link = regular_good_link
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_link()
        page.going_to_busket()
        basket_page = BasketPage(browser,browser.current_url)
        basket_page.should_be_basket_url()
        basket_page.expected_result_not_product_in_busket() #проверяем что нет товаров в корзине
        basket_page.expected_result_not_product_in_busket_notify() #проверяем корзина пустая , нет вспливабщего сообщения

#Тест на переход на страницу логина со странцы конкретного товара
@pytest.mark.login_guest_from_productpage
class TestLoginFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        link = regular_good_link
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

#тесты на которых мы проверяли что селекторы отрабатывают
@pytest.mark.skip
class TestWithErrors():
    #проверяем что после добавления товара у нас не всплывает сообщение о добавоенном товаре
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = promo_link
        page = ProductPage(browser, link)
        page.open()
        page.click_to_cart_button()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    #проверяем что после добавоения товара сообщение о добавленном товаре исчезает
    def test_message_disappeared_after_adding_product_to_basket(browser):
        link = promo_link
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                         # открываем  страницу
        page.click_to_cart_button()
        page.solve_quiz_and_get_code()
        page.should_be_success_message_disappeared()
