import allure
from file_paths import ASSETS_DIR
from pages.receipt_page import ReceiptPage


class TestCreateReceipt:
    @allure.title("Создание нового рецепта")
    @allure.description("Проверка создания рецепта с валидными данными")
    def test_create_receipt(self, driver, reg_and_login_user, receipt_payload):
        with allure.step("Инициализация страницы рецептов"):
            receipt = ReceiptPage(driver)

        with allure.step("Подготовка тестовых данных"):
            img = ASSETS_DIR / 'shrek.webp'

        with allure.step("Создание рецепта через UI"):
            receipt_result = receipt.create_receipt(
                receipt_payload['name'],
                'ф',
                receipt_payload['ingredient_amount'],
                receipt_payload['cooking_time'],
                receipt_payload['description'],
                img
            )

        with allure.step("Проверка успешного создания рецепта"):
            assert receipt_result

        with allure.step("Проверка отображения названия рецепта в карточке"):
            assert receipt.check_name_in_cart(receipt_payload['name'])