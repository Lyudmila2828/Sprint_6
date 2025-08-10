import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_SELECT = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION = (By.XPATH, "//button[@value='{}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DAY_INPUT = (By.CLASS_NAME, "react-datepicker__day--selected")
    PERIOD_SELECT = (By.XPATH, "//div[@class='Dropdown-control']")
    PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнение первой формы заказа')
    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys_to_element(self.NAME_INPUT, name)
        self.send_keys_to_element(self.SURNAME_INPUT, surname)
        self.send_keys_to_element(self.ADDRESS_INPUT, address)
        self.click_element(self.METRO_SELECT)
        self.click_element((self.METRO_OPTION[0], self.METRO_OPTION[1].format(metro)))
        self.send_keys_to_element(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    @allure.step('Метод проверки усешного заказа')
    def is_success_visible(self):
        return self.wait_for_element(self.SUCCESS_MODAL).is_displayed()

    @allure.step('Ожидание появления элемента страницы')    
    def wait_for_order_page(self):
        self.wait_for_element(self.NAME_INPUT, timeout=15)

    @allure.step('Заполнение второй формы хаказа')        
    def fill_second_form(self, date, period, color, comment):
        self.send_keys_to_element(self.DATE_INPUT, date)
        self.click_element(self.DAY_INPUT)
        self.click_element(self.PERIOD_SELECT)
        try:
            self.click_element((self.PERIOD_OPTION[0], self.PERIOD_OPTION[1].format(period)))
        except:
            raise ValueError(f"Период аренды '{period}' не найден")
        if color == "black":
            self.click_element(self.COLOR_BLACK)
        elif color == "grey":
            self.click_element(self.COLOR_GREY)
        else:
            raise ValueError(f"Цвет '{color}' не поддерживается")
        self.send_keys_to_element(self.COMMENT_INPUT, comment)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)