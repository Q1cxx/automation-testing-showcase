from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()   # 本地已装 ChromeDriver
    driver.maximize_window()
    yield driver
    driver.quit()

def test_github_login_title(browser):
    browser.get("https://github.com/login")
    assert "Sign in to GitHub" in browser.title