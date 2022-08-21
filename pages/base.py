from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator, timeout=5):
        WDW(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                        message=f"Cant find element by locator {locator}!").click()

    def enter_text(self, locator, text, timeout=5):
        WDW(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                        message=f"Cant find element by locator {locator}!").send_keys(text)