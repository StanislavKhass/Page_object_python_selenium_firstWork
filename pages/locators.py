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
    AMOUNT_OF_CART = (By.CSS_SELECTOR, "header  .page_inner .row .basket-mini")
    NOTIFY_AMOUNT_OF_CART = (By.CSS_SELECTOR, ".page .page_inner #messages div:nth-child(3) .alertinner p strong")
    AMOUNT_OF_GOOD_PRICE = (By.CSS_SELECTOR, ".product_page .row .product_main p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
