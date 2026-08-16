import time
from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
       self.driver = driver
       self.logout = (By.XPATH,"(//button[normalize-space()='Logout'])[1]")
       self.click_logo = (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/button[1]/div[2]/*[name()='svg'][1]")
       self.settings_option = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[2]")


    def open_logout(self):
        self.driver.find_element(*self.click_logo).click()
        time.sleep(2)
        self.driver.find_element(*self.logout).click()
        time.sleep(3)