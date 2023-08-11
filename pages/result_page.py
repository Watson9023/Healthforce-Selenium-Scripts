from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        result_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultDiv"))
        )
        return result_text.text.split(':')[-1].strip()
