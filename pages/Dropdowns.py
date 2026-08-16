from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_select_counselor(driver):
    dropdown = Select(
        driver.find_element(
            By.XPATH, "//body/div/section/div/div/div/select[1]"
        )
    )

    dropdown.select_by_value("5")

    selected = dropdown.first_selected_option.text

    print("Selected Counselors:", selected)

    assert selected == "Counselors"

    time.sleep(2)


    # self.driver.find_element(*self.counselors).click()
        # time.sleep(2)
        # self.driver.find_element(*self.select_counselors).click()
        # time.sleep(2)