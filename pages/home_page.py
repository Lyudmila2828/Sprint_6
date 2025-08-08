from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    def click_order_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    def get_faq_question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def get_faq_answer_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    def click_faq_question(self, index):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(self.get_faq_question_locator(index))
        element = self.wait_for_element(self.get_faq_question_locator(index))
        self.driver.execute_script("arguments[0].click();", element)