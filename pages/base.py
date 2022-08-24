from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class Base:
    def __init__(self, driver):
        self.driver = driver

    def single_tap_on_element(self, locator, timeout=5):
        actions = TouchAction(self.driver)
        element = WDW(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                        message=f"Cant find element by locator {locator}!")
        actions.tap(element).perform()

    def enter_text(self, locator, text, timeout=5):
        WDW(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                        message=f"Cant find element by locator {locator}!").send_keys(text)

    # def find_element_and_scroll_from_it(self, locator, timeout=5):
    #     actions = TouchAction(self.driver)
    #     actions.