from .base_page import BasePage
from .locators import LoginPageLocators
import time # в начале файла



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        if "login" not in current_url:
            assert False , "Url should have '/login' in it"
        else:
            assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self,email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REG_INPUT_EMAIL).send_keys(email)
        input_pass1 = self.browser.find_element(*LoginPageLocators.REG_INPUT_PASS1).send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.REG_INPUT_PASS2).send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

    def generate_email_and_pass(self):
        email = str(time.time()) + "@fakemail.org"
        password = "TestingStandart"
        return email,password
