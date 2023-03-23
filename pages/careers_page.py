from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage:

    DEPARTMENT_SELECT = (By.CSS_SELECTOR, ":nth-of-type(2) > div > div > button")
    DEPARTMENT_SELECT_OPTIONS = (By.CSS_SELECTOR, "div:first-of-type > div > div:nth-of-type(2) > div > div > div > a")
    LANGUAGE_SELECT = (By.CSS_SELECTOR, ":nth-of-type(3) > div > div > button")
    LANGUAGE_SELECT_OPTIONS = (By.CSS_SELECTOR, ":nth-of-type(3) > div > div > div label")
    JOB_LISTING = (By.CSS_SELECTOR, "div:nth-of-type(2) > div > a")
    BASE_URL = "https://cz.careers.veeam.com/vacancies"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.BASE_URL)

    def maximize_window(self):
        self.driver.maximize_window()

    def select_department(self, department):
        self.select_dropdown_option(self.DEPARTMENT_SELECT, self.DEPARTMENT_SELECT_OPTIONS, department)

    def select_language(self, language):
        self.select_dropdown_option(self.LANGUAGE_SELECT, self.LANGUAGE_SELECT_OPTIONS, language)

    def count_jobs(self):
        job_elements = self.driver.find_elements(*self.JOB_LISTING)
        return len(job_elements)

    def click_button(self, locator):
        self.wait_for_element(locator).click()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def select_dropdown_option(self, button_locator, options_locator, value):
        button = self.wait_for_element(button_locator)
        button.click()

        options = self.driver.find_elements(*options_locator)

        if isinstance(value, list):
            for option in options:
                if option.text in value:
                    option.click()
        else:
            for option in options:
                if option.text == value:
                    option.click()
                    break

