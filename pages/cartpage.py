import pytest
from selene import browser, have, be

from data.Product import Product


class CartPage:

    def find_all_products(self):
        pass

    def remove_product_from_cart(self, product: Product):
        product_cart = self.__get_element_in_cart_by_name(product.name)
        product_cart.element('.remove-from-cart input').click()
        browser.element('.update-cart-button').click()

    def assert_addition_product_in_cart(self, product: Product):
        product_cart = self.__get_element_in_cart_by_name(product.name)
        product_cart.element('.qty input').should(have.value(str(product.count)))

    def assert_remove_product_from_cart(self, product: Product):
        with pytest.raises(AssertionError):
            self.__get_element_in_cart_by_name(product.name)

    def __get_element_in_cart_by_name(self, name: str):
        return browser.all('.cart-item-row').element_by(have.text(name)).should(be.visible)
