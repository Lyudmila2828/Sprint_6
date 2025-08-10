import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import URLCollection

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(f'{URLCollection.SCOOTER_HOME_PAGE}')

    @allure.step('Ожидание появления элемента страницы')
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    @allure.step('Метод ввода текста')
    def send_keys_to_element(self, locator, text):
        self.wait_for_element(locator).send_keys(text)
        
    @allure.step('Метод получения URL')
    def get_url(self):
        return self.driver.current_url
    
    @allure.step('Метод смены вкладки браузера')
    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
    
    @allure.step('Метод ожидания загрузки страницы')    
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_contains(url))
        