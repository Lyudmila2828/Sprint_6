from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.wait_for_element(locator).click()

    def send_keys_to_element(self, locator, text):
        self.wait_for_element(locator).send_keys(text)