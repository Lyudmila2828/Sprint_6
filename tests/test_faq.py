import pytest
import allure
from pages.home_page import HomePage
from data import test_data_for_test_important_questions


@pytest.mark.parametrize("index, expected_text", test_data_for_test_important_questions)
class TestFAQ:
    @allure.title("Check FAQ answer")
    def test_faq_answer(self, driver, index, expected_text):
        page = HomePage(driver)
        page.open()
        page.accept_cookies()
        page.click_faq_question(index)
        answer = page.wait_for_element(page.get_faq_answer_locator(index)).text
        assert answer == expected_text