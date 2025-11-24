from selenium.webdriver.common.by import By

class Locators:
    CREATE_ACCOUNT_BUTTON_HEADER = (By.CSS_SELECTOR, "a[href='/signup']")
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input[name='first_name']")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input[name='last_name']")
    INPUT_USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    CREATE_ACCOUNT_BUTTON_FORM = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
    LOGIN_BUTTON_FORM = (By.XPATH, "//button[contains(.,'Войти')]")
    LOGIN_BUTTON_HEADER = (By.CSS_SELECTOR, "a[href='/signin']")
    LOGOUT_BUTTON_HEADER = (By.XPATH, "//a[contains(.,'Выход')]")
    CREATE_RECEIPT_BUTTON_HEADER = (By.CSS_SELECTOR, "a[href='/recipes/create']")
    CREATE_RECEIPT_BUTTON_FORM = (By.XPATH, "//button[.='Создать рецепт']")
    RECEIPT_NAME = (By.XPATH, "//label[.//div[contains(.,'Название рецепта')]]//input")
    RECEIPT_INGREDIENT = (By.XPATH, "//label[.//div[contains(.,'Ингредиенты')]]//input")
    INGREDIENTS_LIST = (By.CLASS_NAME, "styles_container__3ukwm")
    INGREDIENT_AMOUNT = (By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[.='Добавить ингредиент']")
    RECEIPT_TIME = (By.XPATH, "//label[.//div[contains(.,'Время приготовления')]]//input")
    RECEIPT_DESCRIPTION = (By.XPATH, "//label[.//div[contains(.,'Описание рецепта')]]//textarea")
    ADD_FILE_BUTTON = (By.CLASS_NAME, "styles_fileInput__3HjP3")
    RECEIPT_CARD = (By.CLASS_NAME, "styles_single-card__1yTTj")
    RECEIPT_NAME_IN_CARD = (By.CSS_SELECTOR, ".styles_single-card__header-info__3B9iz h1")






