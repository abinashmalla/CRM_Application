import pytest
from pages.login_page import LoginPage

@pytest.fixture
def setup(driver,username="crm_superuser@gmail.com",password="Crm_@#in_pw267"):
    login_page = LoginPage(driver)
    login_page.open_url("https://crm.mindriserstech.com/login")
    driver.maximize_window()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    yield driver
    driver.quit()