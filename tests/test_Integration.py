import time
from pages.login_page import LoginPage
from pages.Dashboard_page import HomePage
from pages.Report_page import Report_Page
from pages.Settings_admin import Settings_Page
from pages.Add_Lead import Add_Lead
from pages.Add_Next import Add_Next
from pages.Add_Next2 import Add_Next2
from pages.logout import LogoutPage
import pytest

@pytest.mark.parametrize( "username,password",[
    ("crm_superuser@gmail.com","Crm_@#in_pw267"),
])
def test_end_to_end_pages(driver,username,password):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    report_page = Report_Page(driver)
    settings_page = Settings_Page(driver)
    click_logout = LogoutPage(driver)
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

    home_page.click_counselor()
    time.sleep(2)
    home_page.click_Source()
    time.sleep(2)
    home_page.click_Course()
    time.sleep(2)
    home_page.click_Batch()
    time.sleep(2)
    home_page.click_Stage()
    time.sleep(2)
    home_page.click_search_box()
    time.sleep(2)
    home_page.ADD_Title()
    time.sleep(2)
    home_page.show_Added()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[-1])
    report_page.open_report(driver)
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[-1])
    settings_page.open_settings(driver)
    time.sleep(2)

    click_logout.open_logout()
    time.sleep(2)