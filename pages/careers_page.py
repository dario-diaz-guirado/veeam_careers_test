from selenium.webdriver.common.by import By
from .base_page import BasePage

class CareersPage(BasePage):

    DEPARTMENT_SELECT = (By.CSS_SELECTOR, ":nth-of-type(2) > div > div > button")
    DEPARTMENT_SELECT_OPTIONS = (By.CSS_SELECTOR, "div:first-of-type > div > div:nth-of-type(2) > div > div > div > a")
    LANGUAGE_SELECT = (By.CSS_SELECTOR, ":nth-of-type(3) > div > div > button")
    LANGUAGE_SELECT_OPTIONS = (By.CSS_SELECTOR, ":nth-of-type(3) > div > div > div label")
    JOB_LISTING = (By.CSS_SELECTOR, "div:nth-of-type(2) > div > a")
    FILTERS_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Show jobs']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url="https://cz.careers.veeam.com/vacancies"):
        self.driver.get(url)

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
