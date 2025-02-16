import requests

from data import Product

LOGIN = 'example1200@example.com'
PASSWORD = '123456'
BASE_URL = "https://demowebshop.tricentis.com"


def get_auth_coockie():
    name_cookie = 'NOPCOMMERCE.AUTH'
    body = {
        "EMAIL": LOGIN,
        "PASSWORD": PASSWORD
    }
    response = requests.post(url=BASE_URL + '/login', data=body, allow_redirects=False)
    value = response.cookies.get(name_cookie)
    cookie = {"name": name_cookie, "value": value}

    return cookie


def add_product_through_api(product: Product):
    url = f"{BASE_URL}/addproducttocart/catalog/{product.id}/1/{product.count}"
    cookie = get_auth_coockie()

    response = requests.post(url=url, cookies={cookie.get('name'): cookie.get('value')})

    assert response.json()['success'] == True, f'При добавлении товара произошла ошибка: {response.text}'
