import pytest
from selenium import webdriver
from pages.careers_page import CareersPage

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_job_count(browser):
    # Set these variables according to your test requirements
    department = "Research & Development"
    language = ["English"] # You can add more languages at the same time
    expected_job_count = 7  # Replace with the expected job count

    # Initialize the careers page and perform the test
    careers_page = CareersPage(browser)
    careers_page.open()
    careers_page.maximize_window()
    careers_page.select_department(department)
    careers_page.select_language(language)

    # Assert the actual job count matches the expected job count
    actual_job_count = careers_page.count_jobs()
    assert actual_job_count == expected_job_count, f"Expected {expected_job_count} jobs, but found {actual_job_count}"
