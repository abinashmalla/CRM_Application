import time
import pytest
from selenium.webdriver.common.by import By


class Add_Next2:
    def __init__(self,driver):
        self.driver = driver
        self.add_Next_button2 = (By.XPATH,"(//button[normalize-space()='Next'])[1]")
        self.bill_no = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/input[1]")
        self.amount_paid = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[3]/input[1]")
        self.payment_mode = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[4]/select[1]")
        self.select_payment_mode = (By.XPATH,"(//option[@value='1'])[1]")
        self.payment_date = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[5]/input[1]")

        self.discount = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[7]/input[1]")
        self.submit = (By.XPATH,"(//button[normalize-space()='Submit'])[1]")
        self.previous = (By.XPATH,"//button[normalize-space()='Previous']")


    def enter_next_button2(self):
        self.driver.find_element(*self.add_Next_button2).click()
        time.sleep(2)

    @pytest.mark.skip
    def fill_next_info2(self):
        self.driver.find_element(*self.bill_no).click().send_keys("9")
        time.sleep(3)
        self.driver.find_element(*self.amount_paid).click().send_keys("15000")
        time.sleep(2)
        self.driver.find_element(*self.payment_mode).click()
        time.sleep(2)
        self.driver.find_element(*self.select_payment_mode).click()
        time.sleep(2)
        self.driver.find_element(*self.payment_date).click().send_keys("08/01/2026")
        time.sleep(2)
        self.driver.find_element(*self.discount).click().send_keys("20%")
        time.sleep(2)
        self.driver.find_element(*self.submit).click()
        time.sleep(3)