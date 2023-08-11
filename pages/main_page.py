from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.input_box_locator = (By.ID, "number")
        self.calculate_button_locator = (By.ID, "getFactorial")

    def open(self, url):
        self.driver.get(url)

    def input_number(self, number):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.input_box_locator)
        )
        input_box.clear()
        input_box.send_keys(number)

    def click_calculate(self):
        calculate_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.calculate_button_locator)
        )
        calculate_button.click()
