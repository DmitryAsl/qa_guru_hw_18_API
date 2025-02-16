from selene import browser, have, be


class MainPage:

    def open(self):
        browser.open('/')

    def open_product_cart(self):
        browser.element('.ico-cart .cart-label').click()
