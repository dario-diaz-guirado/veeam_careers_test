from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def select_dropdown_option(self, button_locator, options_locator, value):
        button = self.wait_for_element(button_locator)
        button.click()

        options = self.driver.find_elements(*options_locator)
        for option in options:
            if option.text == value:
                option.click()
                break
