import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
import time

@pytest.mark.parametrize( "username,password",[
    ("crm_superuser@gmail.com","Crm_@#in_pw267")
])
@pytest.mark.parametrize("browser", ["chrome", "firefox","ChromiumEdge"])
@pytest.mark.smoke
def test_login(browser, username, password):
    driver = get_driver(browser)
    login_page = LoginPage(driver)
    driver.get("https://crm.mindriserstech.com/login")
    driver.maximize_window()
    time.sleep(2)
    login_page.enter_username(username)
    time.sleep(2)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(2)
    driver.quit()