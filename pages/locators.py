from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    REAL_NAME_GOOD = (By.CSS_SELECTOR, "#content_inner .product_page .row .product_main h1")
    NOTIFY_AFTER_ADD_IN_CART = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
