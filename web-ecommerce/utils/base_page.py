from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        ele = self.wait.until(EC.presence_of_element_located(locator))
        ele.clear(); ele.send_keys(text)

    def text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text