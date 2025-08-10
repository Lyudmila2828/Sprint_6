import pytest
import allure
from data import order_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import URLCollection
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.mark.parametrize("test_data", order_data)
class TestOrder:
    @allure.title("Проверка процесса заказа самоката")
    def test_order_flow_top(self,driver, test_data):
        home_page = HomePage(driver)
        home_page.open()
        order_page = OrderPage(driver)
        home_page.accept_cookies()
        home_page.click_order_top()
        order_page.wait_for_order_page()
        order_page.fill_first_form(
            test_data["first_name"], test_data["second_name"], test_data["address"],
            test_data["metro_station"], test_data["phone_number"]
        )
        order_page.fill_second_form(
            test_data["delivery_date"], test_data["rental_period"], test_data["scooter_color"],
            test_data["courier_comment"]
        )
        assert order_page.is_success_visible(), "Модальное окно успешного заказа не отобразилось"

    @allure.title("Проверка процесса заказа самоката через нижнюю кнопку")
    def test_order_flow_bottom(self, driver, test_data):
        home_page = HomePage(driver)
        home_page.open()
        order_page = OrderPage(driver)
        home_page.accept_cookies()
        home_page.click_order_bottom()
        order_page.wait_for_order_page()
        order_page.fill_first_form(
            test_data["first_name"], test_data["second_name"], test_data["address"],
            test_data["metro_station"], test_data["phone_number"]
        )
        order_page.fill_second_form(
            test_data["delivery_date"], test_data["rental_period"], test_data["scooter_color"],
            test_data["courier_comment"]
        )
        assert order_page.is_success_visible(), "Модальное окно успешного заказа не отобразилось"
