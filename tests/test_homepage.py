from pages.Dashboard_page import HomePage
import time
import pytest
from tests.conftest import setup


@pytest.fixture
def test_login(setup):
    print("test_login")
    time.sleep(4)

@pytest.mark.smoke
def test_HomePage(test_login,driver):
    home_page = HomePage(driver)
    time.sleep(3)
    home_page.click_counselor()
    time.sleep(3)
    home_page.click_Source()
    time.sleep(3)
    home_page.click_Course()
    time.sleep(3)
    home_page.click_Batch()
    time.sleep(3)
    home_page.click_Stage()
    time.sleep(3)
    home_page.click_search_box()
    time.sleep(3)
    home_page.ADD_Title()
    time.sleep(3)
    home_page.show_Added()
    time.sleep(3)
    home_page.show_Results()
    time.sleep(3)