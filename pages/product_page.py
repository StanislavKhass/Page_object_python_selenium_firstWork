from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException
import time

class ProductPage(BasePage):

    #убираем из строки символы, которые не цифры
    def cleaning_price_string(self,str):
        len_buffer_of_string = len(str)
        #Отсекаем то что не является числом
        first_intrace_digit = 0
        for i in range(len_buffer_of_string-1):
            if str[i].isdigit():
                first_intrace_digit = i
                break
        str = str[first_intrace_digit:len_buffer_of_string]

        if str.replace(".", "").isnumeric():
            str = float(str)
        return str

    #проверяем локаторы на наличие перед сохранением ожидаемой суммы
    def check_locators_save_amount_of_good_with_current_cart(self):
        assert self.is_element_present(*ProductPageLocators.AMOUNT_OF_CART), "Cart amount elements is not present"
        assert self.is_element_present(*ProductPageLocators.AMOUNT_OF_GOOD_PRICE), "Amount of good price elements is not present"

    #смотрим сумму в корзине и сумму товара и складываем , возращаем ожидаеммую сумму после добавления товара в корзину
    def save_amount_of_good_with_current_cart(self):
        text_amount_of_cart = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_CART).text
        text_amount_of_cart = text_amount_of_cart.split(":")[1]
        text_amount_of_cart = text_amount_of_cart.split("\n")[0]
        text_amount_of_cart = self.cleaning_price_string(text_amount_of_cart)

        text_amount_of_good_price = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_GOOD_PRICE).text
        text_amount_of_good_price = self.cleaning_price_string(text_amount_of_good_price)

        expected_price = text_amount_of_cart + text_amount_of_good_price
        return expected_price

    #проверяем локатор на наличие перед сохранением названия
    def check_locators_save_name_of_product(self):
        assert self.is_element_present(*ProductPageLocators.REAL_NAME_GOOD), "Name of product elements is not present"

    #сохраняем название товара
    def save_name_of_product(self):
        product_page_goods_name = self.browser.find_element(*ProductPageLocators.REAL_NAME_GOOD)
        return product_page_goods_name.text

    #проверяем что находимся на странице с промо
    def should_be_product_page_url(self):
        current_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        if "promo=" not in current_url:
            assert False , "Url should have '/promo=newYear' in it"
        else:
            assert True

    #проверяем кнопка добавить в карзину присутствует
    def should_cart_button(self):
       assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Cart button is not presented"

    #добавляем товар в корзину
    def click_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    #проверяем локаторы на наличие перед сверкой
    def check_locators_expected_result_good_in_cart_add_notify_same(self):
        assert self.is_element_present(*ProductPageLocators.NOTIFY_AFTER_ADD_IN_CART), "Name of good elements is not present"

    #Название товара совпадает с сообщением после добавления в корзину
    def expected_result_good_in_cart_add_notify_same(self,product_name):
        notify_after_add_in_cart = self.browser.find_element(*ProductPageLocators.NOTIFY_AFTER_ADD_IN_CART)
        assert product_name == notify_after_add_in_cart.text , f"Name of Expected good is different in cart: {product_name}"

    #проверяем локаторы на наличие перед сверкой
    def check_locators_expected_result_good_price_add_notify_same(self):
        assert self.is_element_present(*ProductPageLocators.NOTIFY_AMOUNT_OF_CART), "Amount of good notify elements is not present"

    #проверяем сумму в сплывещем сообщение, что она сходится с ожидаемой суммой
    def expected_result_good_price_add_notify_same(self, expected_price):
        text_amount_of_cart = self.browser.find_element(*ProductPageLocators.NOTIFY_AMOUNT_OF_CART).text
        text_amount_of_cart = self.cleaning_price_string(text_amount_of_cart)
        if expected_price == text_amount_of_cart:
            assert True
        else:
            assert False, f"Totall cart is not right:expected:{expected_price},Current:{text_amount_of_cart}"

    #проверяем что элемента нет на странице
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTIFY_AFTER_ADD_IN_CART), \
           "Success message is presented, but should not be"

    #проверяем что элемент исчет со страницы
    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NOTIFY_AFTER_ADD_IN_CART), \
            "Success message should be disappeared , but it not happend"
