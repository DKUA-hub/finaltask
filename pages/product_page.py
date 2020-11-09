from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProdPage(BasePage):
    def verify_bought_product(self):
        self.solve_quiz_and_get_code()
        self.should_be_bought_product_alert()
        self.should_be_bought_price_alert()

    def buy_product(self):
        buy_btn = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        buy_btn.click()

    def bought_product_should_have_right_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        bought_price = self.alerts[2].text
        assert price == bought_price, f"PRODUCT PRICESS MISMATCH: page price -->> {price} <<-- against -->> {bought_price} <<--"

    def bought_product_should_have_right_name(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        bought_product = self.alerts[0].text
        assert product == bought_product, f"PRODUCT NAMES MISSMATCH: page name -->> {product} <<-- against basket name -->>{bought_product}<<--"


    def should_be_bought_product_alert(self):
        self.alerts = self.browser.find_elements(*ProductPageLocators.INNER_ALERTS)
        assert self.alerts[0], "No 'Product bought' allert message"

    def should_be_bought_price_alert(self):
        assert self.alerts[2], "No 'Price confirmation' allert message"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
