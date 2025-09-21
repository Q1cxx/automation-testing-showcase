from utils.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BTN   = (By.ID, "search-btn")

    def search_product(self, keyword):
        self.send_keys(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BTN)