import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest
from tests.conftest import setup

@pytest.fixture
def test_login(setup,driver):
     print("test_login")
     time.sleep(3)

def test_select_counselor(test_login,driver):
    dropdown = Select(driver.find_element(By.XPATH, "//body/div/section/div/div/div/select[1]"))
    dropdown.select_by_value("5")
    time.sleep(2)
    selected = dropdown.first_selected_option.text
    print("Selected Counselors:", selected)
    time.sleep(2)
    assert selected == "Rabina Koirala"
    time.sleep(2)

def test_select_Sources(test_login,driver):
    dropdown = Select(driver.find_element(By.XPATH, "//body//div//select[2]"))
    dropdown.select_by_visible_text("Direct")
    selected = dropdown.first_selected_option.text
    print("Selected Sources:", selected)
    assert selected == "Direct"
    time.sleep(2)

def test_select_Courses(test_login,driver):
    dropdown = Select(driver.find_element(By.XPATH, "(//select)[3]"))
    dropdown.select_by_visible_text("Quality Assurance Training with AI")
    selected = dropdown.first_selected_option.text
    print("Selected Sources:", selected)
    assert selected == "Quality Assurance Training with AI"
    time.sleep(2)


def test_select_Batch(test_login,driver):
    dropdown = Select(driver.find_element(By.XPATH, "(//select)[4]"))
    dropdown.select_by_visible_text("Asar")
    selected = dropdown.first_selected_option.text
    print("Selected Sources:", selected)
    assert selected == "Asar"
    time.sleep(2)

def test_select_Stage(test_login,driver):
    dropdown = Select(driver.find_element(By.XPATH, "(//select)[5]"))
    dropdown.select_by_visible_text("Enrolled")
    selected = dropdown.first_selected_option.text
    print("Selected Sources:", selected)
    assert selected == "Enrolled"
    time.sleep(2)

