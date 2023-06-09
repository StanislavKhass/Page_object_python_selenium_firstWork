from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_INPUT_EMAIL = (By.CSS_SELECTOR, "#register_form .form-group input#id_registration-email")
    REG_INPUT_PASS1 = (By.CSS_SELECTOR, "#register_form .form-group input#id_registration-password1")
    REG_INPUT_PASS2 = (By.CSS_SELECTOR, "#register_form .form-group input#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    REAL_NAME_GOOD = (By.CSS_SELECTOR, "#content_inner .product_page .row .product_main h1")
    NOTIFY_AFTER_ADD_IN_CART = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    AMOUNT_OF_CART = (By.CSS_SELECTOR, "header  .page_inner .row .basket-mini")
    NOTIFY_AMOUNT_OF_CART = (By.CSS_SELECTOR, ".page .page_inner #messages div:nth-child(3) .alertinner p strong")
    AMOUNT_OF_GOOD_PRICE = (By.CSS_SELECTOR, ".product_page .row .product_main p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner .row .basket-mini .btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, ".content #content_inner #basket_formset")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, ".content #content_inner p")
