from locators import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def login_user(self, email, password):
        self.click_element(Locators.INPUT_EMAIL)
        self.send_keys(Locators.INPUT_EMAIL, email)
        self.click_element(Locators.INPUT_PASSWORD)
        self.send_keys(Locators.INPUT_PASSWORD, password)
        self.click_element(Locators.LOGIN_BUTTON_FORM)
        return self.wait_of_element(Locators.LOGOUT_BUTTON_HEADER)

