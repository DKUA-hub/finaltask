from selenium.webdriver.common.by import By

class MainLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div .product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div .product_main h1")
    BUY_BUTTON = (By.CSS_SELECTOR, '[class = "btn btn-lg btn-primary btn-add-to-basket"]')
    #ACCOUNTED_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    INNER_ALERTS = (By.CSS_SELECTOR, ".alertinner strong")
