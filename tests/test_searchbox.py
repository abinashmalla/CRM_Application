from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from tests.conftest import setup

@pytest.fixture
def test_login(setup,driver):
     print("test_login")
     time.sleep(3)

def test_search(driver,test_login):
    search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Search students'])[1]")))
    search_box.send_keys("Abinash_Malla")
    search_box.click()
    time.sleep(3)
    selected = search_box.text
    print("Selected Counselors:", selected)
    time.sleep(2)

