import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
       self.driver = driver
       self.username_textbox = (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/section[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
       self.password_textbox = (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/section[1]/div[1]/form[1]/div[2]/div[2]/input[1]")
       self.login_button = (By.XPATH,"(//button[normalize-space()='Login'])[1]")

    def open_url(self, url):
        self.driver.get(url)
        time.sleep(1)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        time.sleep(2)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
        time.sleep(2)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()