from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) #создаем обьект для работы с страницей логина
    login_page.should_be_login_page() # Проверяем 3 условия - 1.есть login в ссылке , 2.есть формы логина и 3.регистрации

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#Перед отрицательной проверкой проверяем что такая ссылка есть
def test_guest_add_good_in_basket_and_check_patch(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_cart_button()
    page.should_be_basket_link()
    page.going_to_busket()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.expected_result_product_in_busket()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.going_to_busket()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.expected_result_not_product_in_busket() #проверяем что нет товаров в корзине
    basket_page.expected_result_not_product_in_busket_notify() #проверяем корзина пустая
