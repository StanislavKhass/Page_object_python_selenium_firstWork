from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

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

    def save_amount_of_good_with_current_cart(self):
        #Обработчик для сохранения строки в число для последующей обработки
        #Сохраняем и отсекам от букв строку , оставляем только цифры
        text_amount_of_cart = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_CART).text
        text_amount_of_cart = text_amount_of_cart.split(":")[1]
        text_amount_of_cart = text_amount_of_cart.split("\n")[0]
        text_amount_of_cart = self.cleaning_price_string(text_amount_of_cart)

        text_amount_of_good_price = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_GOOD_PRICE).text
        text_amount_of_good_price = self.cleaning_price_string(text_amount_of_good_price)

        expected_price = text_amount_of_cart + text_amount_of_good_price
        return expected_price

    def save_name_of_product(self):
        product_page_goods_name = self.browser.find_element(*ProductPageLocators.REAL_NAME_GOOD)
        return product_page_goods_name.text

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

    def expected_result_good_in_cart_add_notify_same(self,product_name):
        notify_after_add_in_cart = self.browser.find_element(*ProductPageLocators.NOTIFY_AFTER_ADD_IN_CART)
        assert product_name == notify_after_add_in_cart.text , f"Name of Expected good is different in cart: {product_name}"

    def expected_result_good_price_add_notify_same(self, expected_price):
        text_amount_of_cart = self.browser.find_element(*ProductPageLocators.NOTIFY_AMOUNT_OF_CART).text

        text_amount_of_cart = self.cleaning_price_string(text_amount_of_cart)

        if expected_price == text_amount_of_cart:
            #time.sleep(1000)
            assert True
        else:
            assert False, f"Totall cart is not right:expected:{expected_price},Current:{text_amount_of_cart}"
