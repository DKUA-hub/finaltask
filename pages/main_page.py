from .base_page import BasePage
from .locators import MainLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
#import selenium.webdriver.remote.webdriver

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainLocators.LOGIN_LINK), "No login link"
