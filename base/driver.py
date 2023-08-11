from selenium import webdriver


class Driver:
    def __init__(self, driver_path, browser_name):
        self.driver_path = driver_path
        self.browser_name = browser_name

    def create_driver(self):
        if self.browser_name.lower() == 'chrome':
            return self._create_chrome_driver()
        elif self.browser_name.lower() == 'firefox':
            return self._create_firefox_driver()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

    def _create_chrome_driver(self):
        options = webdriver.ChromeOptions()
        # Add any desired options to the options object

        # Example option: Headless mode
        # options.add_argument('--headless')

        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        driver.maximize_window()
        return driver

    def _create_firefox_driver(self):
        options = webdriver.FirefoxOptions()
        # Add any desired options to the options object

        # Example option: Headless mode
        # options.headless = True

        # Disable browser automation message
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Firefox(executable_path=self.driver_path, options=options)
        driver.maximize_window()
        return driver
