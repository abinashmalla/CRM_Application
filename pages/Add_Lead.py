import time
from selenium.webdriver.common.by import By

class Add_Lead:
    def __init__(self,driver):
        self.driver = driver
        self.add_button = (By.XPATH, "//button[normalize-space()='+ Add Lead']")
        self.student_name = (By.XPATH, "//input[@placeholder='Enter student name']")
        self.phone = (By.XPATH,"//input[@placeholder='Enter phone']")
        self.email = (By.XPATH,"//input[@placeholder='Enter email']")
        self.dob = (By.XPATH,"//input[@name='dateOfBirth']")
        self.guardian_name = (By.XPATH,"//input[@placeholder='Enter guardian name']")
        self.guardian_phone = (By.XPATH,"//input[@placeholder='+977']")
        self.college = (By.XPATH,"//input[@placeholder='Enter college name']")
        self.select_level = (By.XPATH,"//select[@name='studyLevel']")
        self.select_option = (By.XPATH,"(//option[@value='3'])[1]")

    def enter_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def Fill_Info(self):
        self.driver.find_element(*self.student_name).send_keys("Abinash_Malla")
        time.sleep(2)
        self.driver.find_element(*self.phone).send_keys("+9779849658392")
        time.sleep(2)
        self.driver.find_element(*self.email).send_keys("abinashm498@gmail.com")
        time.sleep(2)
        self.driver.find_element(*self.dob).send_keys("08/01/2026")
        time.sleep(2)
        self.driver.find_element(*self.guardian_name).send_keys("Pratime_Malla")
        time.sleep(2)
        self.driver.find_element(*self.guardian_phone).send_keys("+977 9849658392")
        time.sleep(2)
        self.driver.find_element(*self.college).send_keys("Trinity")
        time.sleep(2)
        self.driver.find_element(*self.select_level).click()
        time.sleep(2)
        self.driver.find_element(*self.select_option).click()
        time.sleep(2)