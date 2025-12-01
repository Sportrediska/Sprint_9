import allure
from pages.login_page import LoginPage


class TestLoginUser:
    @allure.title("Успешный логин пользователя")
    @allure.description("Проверка авторизации зарегистрированного пользователя")
    def test_login_user_success(self, driver, reg_user):
        with allure.step("Инициализация страницы логина"):
            login = LoginPage(driver)

        with allure.step("Выполнение процедуры логина"):
            result = login.login_user(reg_user['user_name'], reg_user['password'])

        with allure.step("Проверка успешного логина"):
            assert result