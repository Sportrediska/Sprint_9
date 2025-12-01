from locators import Locators
from pages.base_page import BasePage


class ReceiptPage(BasePage):
    def create_receipt(self, name, ingredient_value, ingredient_amount, cooking_time, description, img):
        self.click_element(Locators.CREATE_RECEIPT_BUTTON_HEADER)
        self.wait_of_element(Locators.RECEIPT_NAME)
        self.click_element(Locators.RECEIPT_NAME)
        self.send_keys(Locators.RECEIPT_NAME, name)
        self.click_element(Locators.RECEIPT_INGREDIENT)
        self.send_keys(Locators.RECEIPT_INGREDIENT, ingredient_value)
        self.wait_of_element(Locators.INGREDIENTS_LIST)
        self.click_by_index(Locators.INGREDIENTS_LIST, 0)
        self.click_element(Locators.INGREDIENT_AMOUNT)
        self.send_keys(Locators.INGREDIENT_AMOUNT, ingredient_amount)
        self.click_element(Locators.ADD_INGREDIENT_BUTTON)
        self.click_element(Locators.RECEIPT_TIME)
        self.send_keys(Locators.RECEIPT_TIME, cooking_time)
        self.click_element(Locators.RECEIPT_DESCRIPTION)
        self.send_keys(Locators.RECEIPT_DESCRIPTION, description)
        self.send_keys(Locators.ADD_FILE_BUTTON, str(img))
        self.click_element(Locators.CREATE_RECEIPT_BUTTON_FORM)
        return self.wait_of_element(Locators.RECEIPT_CARD)

    def check_name_in_card(self, name):
        locator_name = self.get_text_by_locator(Locators.RECEIPT_NAME_IN_CARD)
        return name == locator_name


