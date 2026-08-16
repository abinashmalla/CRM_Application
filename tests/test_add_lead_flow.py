
import time
from pages.login_page import LoginPage
from pages.Add_Lead import Add_Lead
from pages.Add_Next import Add_Next

import pytest

@pytest.mark.parametrize( "username,password",[
    ("crm_superuser@gmail.com","Crm_@#in_pw267"),
])
@pytest.mark.smoke
def test_ADD_Lead_workflow(driver,username,password):
    login_page = LoginPage(driver)
    AddLead_page = Add_Lead(driver)
    Add_Next_page = Add_Next(driver)

    login_page.open_url("https://crm.mindriserstech.com/login")
    driver.maximize_window()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(3)
    AddLead_page.enter_add_button()
    AddLead_page.Fill_Info()
    time.sleep(3)
    Add_Next_page.enter_next_button()
    time.sleep(2)
    Add_Next_page.fill_next_info()
    time.sleep(3)
