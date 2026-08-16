import time
from selenium.webdriver.common.by import By

class Students_Details:
    def __init__(self, driver):
        self.driver = driver
        self.abi_malla = (By.XPATH, "//td[normalize-space()='Abinash_Malla']")
        self.education_level = (By.XPATH,"//span[normalize-space()='Education Level']")
        self.select_edu_level = (By.XPATH,"//option[normalize-space()='Masters']")
        self.notes =(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[2]/main[1]/div[1]/button[2]")
        self.Call_log = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[2]/main[1]/div[1]/button[3]")
        self.transaction = (By.XPATH,"(//button[normalize-space()='Transactions'])[1]")
        self.edit = (By.XPATH,"//button[@title='Edit info']//*[name()='svg']")
        self.add_transaction = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[2]/main[1]/div[2]/section[1]/div[2]/button[1]")
        self.cancel_button=(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[2]/main[1]/div[2]/div[1]/div[1]/form[1]/div[5]/button[1]")

    def open_students_level(self):
        self.driver.find_element(*self.abi_malla).click()
        time.sleep(2)
        self.driver.find_element(*self.edit).click()
        time.sleep(2)
        self.driver.find_element(*self.education_level).click()
        time.sleep(2)
        self.driver.find_element(*self.select_edu_level).click()
        time.sleep(2)
        self.driver.find_element(*self.notes).click()
        time.sleep(2)
        self.driver.find_element(*self.Call_log).click()
        time.sleep(2)
        self.driver.find_element(*self.transaction).click()
        time.sleep(2)
        self.driver.find_element(*self.add_transaction).click()
        time.sleep(2)
        self.driver.find_element(*self.cancel_button).click()
        time.sleep(2)