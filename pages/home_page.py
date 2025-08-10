import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод принятия куков')
    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    @allure.step('Кликаем по кнопке "Заказать" вверху страницы')
    def click_order_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_order_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    @allure.step('Кликаем по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step('Кликаем по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step('Метод возвращения локатора для вопросов с использованием индекса')
    def get_faq_question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    @allure.step('Метод возвращения локатора для ответов с использованием индекса')
    def get_faq_answer_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    @allure.step('Кликаем на вопросы')
    def click_faq_question(self, index):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(self.get_faq_question_locator(index))
        element = self.wait_for_element(self.get_faq_question_locator(index))
        self.driver.execute_script("arguments[0].click();", element)