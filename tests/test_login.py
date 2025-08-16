import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Login Tests")
@allure.story("Valid Login")
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()
    assert "You logged into a secure area!" in login_page.get_flash_message()

@allure.feature("Login Tests")
@allure.story("Invalid Login")
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("wronguser")
    login_page.enter_password("wrongpass")
    login_page.click_login()
    assert "Your username is invalid!" in login_page.get_flash_message()

@allure.feature("Login Tests")
@allure.story("Empty Credentials")
def test_empty_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()
    assert "Your username is invalid!" in login_page.get_flash_message()
