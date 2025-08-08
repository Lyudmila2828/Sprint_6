import pytest
import allure
from data import order_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import URLCollection


@pytest.mark.parametrize("data", order_data)
class TestOrder:
    @allure.title("Проверка процесса заказа самоката")
    def test_order_flow_top(self, home_page, order_page, data):
        home_page.accept_cookies()
        home_page.click_order_top()
        order_page.wait_for_order_page()
        order_page.fill_first_form(
            data["first_name"], data["second_name"], data["address"],
            data["metro_station"], data["phone_number"]
        )
        order_page.fill_second_form(
            data["delivery_date"], data["rental_period"], data["scooter_color"],
            data["courier_comment"]
        )
        assert order_page.is_success_visible(), "Модальное окно успешного заказа не отобразилось"

    @allure.title("Проверка процесса заказа самоката через нижнюю кнопку")
    def test_order_flow_bottom(self, home_page, order_page, data):
        home_page.accept_cookies()
        home_page.click_order_bottom()
        order_page.wait_for_order_page()
        order_page.fill_first_form(
            data["first_name"], data["second_name"], data["address"],
            data["metro_station"], data["phone_number"]
        )
        order_page.fill_second_form(
            data["delivery_date"], data["rental_period"], data["scooter_color"],
            data["courier_comment"]
        )
        assert order_page.is_success_visible(), "Модальное окно успешного заказа не отобразилось"
        

@allure.title("Переход на главную страницу по логотипу Самоката")
def test_scooter_logo(home_page):
    home_page.accept_cookies()
    home_page.click_order_top()
    home_page.click_scooter_logo()
    assert URLCollection.SCOOTER_HOME_PAGE == home_page.driver.current_url

@allure.title("Переход на Дзен по логотипу Яндекса")
def test_yandex_logo(home_page):
    home_page.accept_cookies()
    home_page.click_order_top()
    home_page.click_yandex_logo()
    home_page.driver.switch_to.window(home_page.driver.window_handles[1])
    WebDriverWait(home_page.driver, 15).until(EC.url_contains("dzen.ru"))
    assert "dzen.ru" in home_page.driver.current_url