from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    amount_of_cart = 0
    curent_amount_of_good = 0

    def save_amount_of_cart(self):
        #Обработчик для сохранения строки в число для последующей обработки
        #Сохраняем и отсекам от букв строку , оставляем только цифры
        text_amount_of_cart = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_CART).text
        text_amount_of_cart = text_amount_of_cart.split(":")[1]
        text_amount_of_cart = text_amount_of_cart.split("\n")[0]
        len_amount_of_cart = len(text_amount_of_cart)
        #Отсекаем то что не является числом
        first_intrace_digit = 0
        for i in range(len_amount_of_cart-1):
            if text_amount_of_cart[i].isdigit():
                first_intrace_digit = i
                break
        text_amount_of_cart = text_amount_of_cart[first_intrace_digit:len_amount_of_cart]
        #Проверяем что сохранили
        if text_amount_of_cart.replace(".", "").isnumeric():
            self.amount_of_cart = float(text_amount_of_cart)
            assert True
        else:
            assert False, f"Amount in cart shoud be digit:{text_amount_of_cart}"

    def save_amount_of_good_price(self):
        text_amount_of_good_price = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_GOOD_PRICE).text

        len_amount_of_good_price = len(text_amount_of_good_price)
        #Отсекаем то что не является числом
        first_intrace_digit = 0
        for i in range(len_amount_of_good_price-1):
            if text_amount_of_good_price[i].isdigit():
                first_intrace_digit = i
                break
        text_amount_of_good_price = text_amount_of_good_price[first_intrace_digit:len_amount_of_good_price]

        #Проверяем что сохранили число
        if text_amount_of_good_price.replace(".", "").isnumeric():
            self.curent_amount_of_good = float(text_amount_of_good_price)
            assert True
        else:
            assert False, f"Amount of good price shoud be digit:{text_amount_of_good_price}"

    def should_be_product_page_url(self):
        current_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        if "promo=" not in current_url:
            assert False , "Url should have '/promo=newYear' in it"
        else:
            assert True

    def should_cart_button(self):
       assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Cart button is not presented"

    def click_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def expected_result_good_in_cart_info_check(self):
        product_page_goods_name = self.browser.find_element(*ProductPageLocators.REAL_NAME_GOOD)
        notify_after_add_in_cart = self.browser.find_element(*ProductPageLocators.NOTIFY_AFTER_ADD_IN_CART)
        assert product_page_goods_name.text == notify_after_add_in_cart.text , "Name of Expected good is different in cart."

    def expected_result_good_price_add_to_cart(self):
        text_amount_of_cart = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_CART).text
        text_amount_of_cart = text_amount_of_cart.split(":")[1]
        text_amount_of_cart = text_amount_of_cart.split("\n")[0]
        len_amount_of_cart = len(text_amount_of_cart)

        first_intrace_digit = 0
        for i in range(len_amount_of_cart-1):
            if text_amount_of_cart[i].isdigit():
                first_intrace_digit = i
                break
        text_amount_of_cart = text_amount_of_cart[first_intrace_digit:len_amount_of_cart]

        if text_amount_of_cart.replace(".", "").isnumeric():
            current_amount_of_cart = float(text_amount_of_cart)

        expected_total_price_cart = self.amount_of_cart + self.curent_amount_of_good
        if expected_total_price_cart == current_amount_of_cart:
            assert True
        else:
            assert False, f"Totall cart is not right:expected:{expected_total_price_cart},Current:{current_amount_of_cart}"
