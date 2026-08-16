import time
from selenium.webdriver.common.by import By

class Settings_Page:
    def __init__(self, driver):
       self.driver = driver
       self.click_logo = (By.XPATH, "(//*[name()='svg'][@class='lucide lucide-user h-5 w-5 text-gray-400'])[1]")
       self.settings_option = (By.XPATH, "//button[@class='flex w-full items-center gap-3 px-4 py-2 text-sm text-gray-700 transition-colors hover:bg-gray-50']")
       self.batch = (By.CSS_SELECTOR,".flex.items-center.gap-2.rounded-xl.px-4.py-2.text-sm.font-medium.transition.bg-white.text-green-700.shadow-sm")

       self.courses=(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[2]/div[2]/button[3]")
       self.all=(By.XPATH,"//div[@class='mt-8 flex w-fit flex-wrap gap-2 rounded-2xl bg-slate-200/60 p-2']")
       self.level = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[2]/div[2]/div[2]/button[4]")
       self.add_new_level = (By.XPATH,"")

    def open_settings(self, driver):
        self.driver.find_element(*self.click_logo).click()
        time.sleep(2)
        self.driver.find_element(*self.settings_option).click()
        time.sleep(2)
        self.driver.find_element(*self.all).click()
        time.sleep(2)
        self.driver.find_element(*self.batch).click()
        time.sleep(2)
        self.driver.find_element(*self.courses).click()
        time.sleep(2)
        self.driver.find_element(*self.level).click()
        time.sleep(2)
        # self.driver.find_element(*self.add_new_level).click()
        # time.sleep(4)