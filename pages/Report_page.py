import time

from selenium.webdriver.common.by import By


class Report_Page:
    def __init__(self, driver):
       self.driver = driver
       self.click_Report_button = (By.XPATH, "//a[normalize-space()='Report']")
       self.all_dates = (By.XPATH,"//button[@class='flex min-w-0 flex-1 items-center gap-2 px-3 py-2.5 text-left']")
       self.start_date = (By.XPATH,"(//button[contains(@class,'text-[#344054] hover:bg-[#EDF6F1]')][normalize-space()='1'])[1]")
       self.end_date = (By.XPATH,"//button[normalize-space()='10']")
       self.all_sources = (By.XPATH,"//body/div[@id='root']/section[contains(@class,'min-h-screen')]/div[contains(@class,'min-h-screen px-10 py-5')]/div[contains(@class,'mb-8 grid grid-cols-2 gap-4 rounded-2xl bg-[#EBF5F0] p-5 lg:grid-cols-4')]/div[2]/div[1]/div[1]")
       self.direct = (By.XPATH,"//div[normalize-space()='Direct']")
       self.all_courses = (By.XPATH,"//div[contains(@class,'flex items-center gap-2 truncate text-[13px] font-medium')][normalize-space()='All Course']")
       self.all_staffs = (By.XPATH,"//body/div[@id='root']/section[contains(@class,'min-h-screen')]/div[contains(@class,'min-h-screen px-10 py-5')]/div[contains(@class,'mb-8 grid grid-cols-2 gap-4 rounded-2xl bg-[#EBF5F0] p-5 lg:grid-cols-4')]/div[4]/div[1]/div[1]")
       self.click_all_Counselors = (By.XPATH,"//span[@class='truncate']")
       self.search_Counselor = (By.XPATH,"//input[@placeholder='Search counselor...']")
       self.select_Counselor = (By.XPATH,"(//span[@class='text-[12px] font-medium text-gray-700'])[1]")

    def open_report(self, driver):
        self.driver.find_element(*self.click_Report_button).click()
        time.sleep(3)
        self.driver.find_element(*self.all_dates).click()
        time.sleep(2)
        self.driver.find_element(*self.start_date).click()
        time.sleep(2)
        self.driver.find_element(*self.end_date).click()
        time.sleep(2)
        self.driver.find_element(*self.all_sources).click()
        time.sleep(2)
        self.driver.find_element(*self.direct).click()
        time.sleep(2)
        self.driver.find_element(*self.all_courses).click()
        time.sleep(2)
        self.driver.find_element(*self.all_staffs).click()
        time.sleep(2)
        self.driver.find_element(*self.click_all_Counselors).click()
        time.sleep(2)
        self.driver.find_element(*self.search_Counselor).send_keys("Asmita")
        time.sleep(2)
        self.driver.find_element(*self.select_Counselor).click()
        time.sleep(4)