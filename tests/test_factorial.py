import time
import unittest
import configparser
from base.driver import Driver
from pages.main_page import MainPage
from pages.result_page import ResultPage

config = configparser.ConfigParser()
config.read("tests/config.ini")

class TestFactorialCalculation(unittest.TestCase):
    base_url = config.get("Application", "base_url")
    driver_path = config.get("Driver", "driver_path")
    browser_name = config.get("Driver", "browser_name")

    @classmethod
    def setUpClass(cls):
        cls.driver_manager = Driver(cls.driver_path, cls.browser_name)
        cls.driver = cls.driver_manager.create_driver()

    @classmethod
    def tearDownClass(cls):
        # Add a delay to see the output before quitting
        time.sleep(5)  # Wait for 5 seconds
        cls.driver.quit()

    def test_factorial_calculation(self):
        main_page = MainPage(self.driver)

        # Open the web application
        main_page.open(self.base_url)  # Use self.base_url here

        # Rest of your test logic
        number_to_input = "7"
        main_page.input_number(number_to_input)
        print(f"Inputting number: {number_to_input}")

        main_page.click_calculate()

        result_page = ResultPage(self.driver)
        calculated_result = result_page.get_result()
        print(f"Calculated result: {calculated_result}")

        expected_result = config.get("ExpectedResults", "factorial_7")
        self.assertEqual(calculated_result, expected_result)

if __name__ == "__main__":
    unittest.main()
