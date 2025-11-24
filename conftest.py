from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.register_user_page import RegisterUserPage
from urls import BASE_URL
from mimesis import Food
from mimesis.locales import Locale

@pytest.fixture
def register_user_method(driver):
    return RegisterUserPage(driver)

@pytest.fixture
def login_user_method(driver):
    return LoginPage(driver)

@pytest.fixture
def random_user_payload_for_create():
    fake = Faker('ru_RU')
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'user_name': fake.user_name(),
        'email': fake.email(),
        'password': fake.password()
    }

@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)

    yield driver
    driver.quit()

@pytest.fixture
def reg_user(register_user_method, random_user_payload_for_create):
    register_user_method.register_user(**random_user_payload_for_create)
    return random_user_payload_for_create

@pytest.fixture
def reg_and_login_user(login_user_method, reg_user):
    login_user_method.login_user(reg_user['user_name'], reg_user['password'])


@pytest.fixture
def receipt_payload():
    fake = Faker('ru_RU')
    food = Food(locale=Locale.RU)
    return {
        'name': food.dish(),
        'ingredient_amount': fake.random_int(min=5, max=500),
        'cooking_time': fake.random_int(min=10, max=120),
        'description': fake.text(max_nb_chars=200)
    }