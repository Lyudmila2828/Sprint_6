import allure
from pages.home_page import HomePage
from url import URLCollection

class TestLogo:
    @allure.title("Переход на главную страницу по логотипу Самоката")
    def test_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()
        home_page.click_order_top()
        home_page.click_scooter_logo()
        assert URLCollection.SCOOTER_HOME_PAGE == home_page.get_url()

    @allure.title("Переход на Дзен по логотипу Яндекса")
    def test_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()
        home_page.click_yandex_logo()
        home_page.switch_window(1)
        home_page.wait_for_url(URLCollection.YANDEX_HOME_PAGE)
        assert URLCollection.YANDEX_HOME_PAGE == home_page.get_url()