import time
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
       self.driver = driver
       self.counselors = (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/div[2]/div[3]/div[1]/select[1]")
       self.select_counselors=(By.XPATH, "(//option[@value='6'])[1]")
       self.Sources = (By.XPATH, "//body//div//select[2]")
       self.select_Sources=(By.XPATH, "//option[@value='Direct']")
       self.Courses = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[3]/div[1]/select[3]")
       self.select_Courses=(By.XPATH, "/html[1]/body[1]/div[1]/section[1]/div[2]/div[3]/div[1]/select[3]")
       self.Batch = (By.XPATH, "//body//div//select[4]")
       self.select_Batch=(By.XPATH, "//option[@value='Shrawan']")
       self.Stage = (By.XPATH, "//body//div//select[5]")
       self.select_Stage=(By.XPATH, "//option[@value='true']")
       self.search_box = (By.XPATH, "//input[@placeholder='Search students']")
       self.add_title = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[3]/div[1]/div[3]/button[1]/*[name()='svg'][1]")
       self.close = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/button[1]/*[name()='svg'][1]")
       self.show_added=(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[3]/div[1]/div[3]/button[2]/*[name()='svg'][1]")
       self.results=(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[3]/div[1]/div[3]/button[3]/*[name()='svg'][1]")

    def click_counselor(self):
        self.driver.find_element(*self.counselors).click()
        time.sleep(2)
        self.driver.find_element(*self.select_counselors).click()
        time.sleep(2)

    def click_Source(self):
        self.driver.find_element(*self.Sources).click()
        time.sleep(2)
        self.driver.find_element(*self.select_Sources).click()

    def click_Course(self):
        self.driver.find_element(*self.Courses).click()
        time.sleep(2)
        self.driver.find_element(*self.select_Courses).click()

    def click_Batch(self):
        self.driver.find_element(*self.Batch).click()
        time.sleep(2)
        self.driver.find_element(*self.select_Batch).click()

    def click_Stage(self):
        self.driver.find_element(*self.Stage).click()
        time.sleep(2)
        self.driver.find_element(*self.select_Stage).click()

    def click_search_box(self):
        self.driver.find_element(*self.search_box).send_keys("werty")
        time.sleep(2)

    def ADD_Title(self):
        self.driver.find_element(*self.add_title).click()
        time.sleep(2)
        self.driver.find_element(*self.close).click()
        time.sleep(3)


    def show_Added(self):
        self.driver.find_element(*self.show_added).click()
        time.sleep(2)

    def show_Results(self):
        self.driver.find_element(*self.results).click()
        time.sleep(2)