import time
import pytest
from tests.conftest import setup

@pytest.mark.smoke
def test_login(setup,driver):
     print("test_login")
     time.sleep(3)
     if "dashboard" in driver.current_url:
         print("Login successful (Landing on the page)")
     else:
         print("login unsuccessfull")









