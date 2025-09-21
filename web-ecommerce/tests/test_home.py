import pytest
from selenium import webdriver
from utils.config import BASE_URL, HEADLESS
from pages.home_page import HomePage

@pytest.fixture(scope="class")
def driver():
    opt = webdriver.ChromeOptions()
    opt.headless = HEADLESS
    dr = webdriver.Chrome(options=opt)
    dr.get(BASE_URL)
    yield dr
    dr.quit()

class TestHome:
    def test_search(self, driver):
        HomePage(driver).search_product("phone")
        assert "phone" in driver.page_source.lower()