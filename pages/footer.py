import time
from selenium.webdriver.common.by import By

class FooterPage:
    def __init__(self, driver):
       self.driver = driver
       self.show_10 = (By.XPATH, "//select[@class='rounded border border-gray-200 p-1 outline-none']")
       self.select_next = (By.XPATH,"//button[normalize-space()='Next >']")

    def open_show(self):

        self.driver.find_element(By.XPATH, self.show_10).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_next).click()
        time.sleep(2)