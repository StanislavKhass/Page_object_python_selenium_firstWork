from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page_url(self):
        current_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        if "promo=newYear" not in current_url:
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
