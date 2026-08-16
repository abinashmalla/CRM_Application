import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.footer import FooterPage
import pytest


@pytest.mark.parametrize( "username,password",[
     ("crm_superuser@gmail.com","Crm_@#in_pw267"),
 ])
@pytest.mark.smoke
def test_setup(driver,username,password):
    login_page = LoginPage(driver)
    footer = FooterPage(driver)
    login_page.open_url("https://crm.mindriserstech.com/login")
    driver.maximize_window()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(3)
    x = 0
    while True:
         x += 1
         driver.execute_script("scrollBy(0,50)")
         time.sleep(0.10)
         if x > 100:
             break
    element = driver.find_element(By.XPATH, "//select[@class='rounded border border-gray-200 p-1 outline-none']")
    element.click()
    time.sleep(2)
    element1 = driver.find_element(By.XPATH,"//button[normalize-space()='Next >']")
    element1.click()
    time.sleep(3)