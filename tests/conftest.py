import allure
import pytest
from selenium import webdriver
from selene import browser
from pages.mainpage import MainPage
from helpers.api_methods import get_auth_coockie


@pytest.fixture(autouse=True)
def browser_config():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.driver_options = driver_options
    yield
    browser.quit()


@pytest.fixture()
@allure.step('Set AUTH coookie')
def browser_with_auth(browser_config):
    main_page = MainPage()
    cookie = get_auth_coockie()

    main_page.open()
    browser.driver.add_cookie(cookie)
    main_page.open()
