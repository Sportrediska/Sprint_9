import allure
from pages.register_user_page import RegisterUserPage


class TestRegisterUser:
    @allure.title("Успешная регистрация пользователя")
    @allure.description("Проверка регистрации нового пользователя в системе")
    def test_register_user_success(self, driver, random_user_payload_for_create):
        with allure.step("Инициализация страницы регистрации"):
            register = RegisterUserPage(driver)

        with allure.step("Заполнение данных пользователя"):
            result = register.register_user(**random_user_payload_for_create)

        with allure.step("Проверка успешной регистрации"):
            assert result