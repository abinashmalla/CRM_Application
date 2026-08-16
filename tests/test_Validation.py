import os
import time
import pytest

@pytest.fixture
def test_login(setup):
    print("test_login")
    time.sleep(4)

@pytest.mark.smoke
def test_login_Validation(driver,test_login):
    if "https://crm.mindriserstech.com/dashboard" in driver.current_url:
        print("Login successful (Landing on the page)")
    else:
         print("login unsuccessfull")

    # if "Dashboard" in driver.current_url:
    #     print("Login successful (Landing on the page)")
    # else:
    #      print("login unsuccessfull")