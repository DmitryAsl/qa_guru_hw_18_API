from helpers.api_methods import add_product_through_api
from data.Product import product_1, product_2

from pages.cartpage import CartPage
from pages.mainpage import MainPage


class TestOperationsProductsInCart:
    mainpage = MainPage()
    cartpage = CartPage()

    def test_add_product_in_cart(self, browser_with_auth):
        add_product_through_api(product_1)
        try:
            self.mainpage.open_product_cart()
            self.cartpage.assert_addition_product_in_cart(product_1)
        finally:
            # удаляем продукт для последующих прогонов теста, т.к проверяется количество
            self.cartpage.remove_product_from_cart(product_1)

    def test_remove_product_from_cart(self, browser_with_auth):
        add_product_through_api(product_2)
        self.mainpage.open_product_cart()

        self.cartpage.remove_product_from_cart(product_2)
        self.cartpage.assert_remove_product_from_cart(product_2)
