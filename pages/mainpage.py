from selene import browser, have, be
import allure

class MainPage:

    @allure.step('Open main page')
    def open(self):
        browser.open('/')

    @allure.step('Open cart page')
    def open_product_cart(self):
        browser.element('.ico-cart .cart-label').click()
