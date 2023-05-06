from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        if "basket" not in current_url:
            assert False , "Url should have 'basket' in it"
        else:
            assert True

    def expected_result_product_in_busket(self):
        assert self.is_element_present(*BasketLocators.BASKET_CONTENT),\
           "No goods in basket , checking patch link, need for next test"

    def expected_result_not_product_in_busket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_CONTENT),\
           "Some goods in basket , but shoud not happend"

    def expected_result_not_product_in_busket_notify(self):
        assert self.is_element_present_wait(*BasketLocators.BASKET_IS_EMPTY) , \
           "No notifi about empty cart, but should not be"
