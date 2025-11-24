from locators import Locators
from pages.base_page import BasePage


class RegisterUserPage(BasePage):
    def register_user(self, first_name, last_name, user_name, email, password):
        self.click_element(Locators.CREATE_ACCOUNT_BUTTON_HEADER)
        self.wait_of_element(Locators.CREATE_ACCOUNT_BUTTON_FORM)
        self.click_element(Locators.INPUT_FIRST_NAME)
        self.send_keys(Locators.INPUT_FIRST_NAME, first_name)
        self.click_element(Locators.INPUT_LAST_NAME)
        self.send_keys(Locators.INPUT_LAST_NAME, last_name)
        self.click_element(Locators.INPUT_USERNAME)
        self.send_keys(Locators.INPUT_USERNAME, user_name)
        self.click_element(Locators.INPUT_EMAIL)
        self.send_keys(Locators.INPUT_EMAIL, email)
        self.click_element(Locators.INPUT_PASSWORD)
        self.send_keys(Locators.INPUT_PASSWORD, password)
        self.click_element(Locators.CREATE_ACCOUNT_BUTTON_FORM)
        return self.wait_of_element(Locators.LOGIN_BUTTON_FORM)