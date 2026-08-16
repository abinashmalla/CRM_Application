import time
from pages.login_page import LoginPage
import pytest
from pages.Students_Details import Students_Details

@pytest.fixture
def test_login(setup):
    print("test_login")
    time.sleep(4)

@pytest.mark.smoke
def test_students_Details(test_login,driver):
    student_details = Students_Details(driver)
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(3)
    student_details.open_students_level()
    time.sleep(3)