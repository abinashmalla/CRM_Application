import pytest
import time
from tests.conftest import setup
from pages.Report_page import Report_Page


@pytest.fixture
def test_login(setup):
    print("test_login")
    time.sleep(4)

def test_report_page(test_login,driver):
    reports = Report_Page(driver)
    reports.open_report(driver)
    x = 0
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break