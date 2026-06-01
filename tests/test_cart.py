from pages.login_page import LoginPage
from pages.home_page import HomePage    
from pages.cart_page import CartPage
from data.test_data import *

def test_add_to_Cart(page):

    login = LoginPage(page)
    home = HomePage(page)
    cart = CartPage(page)

    login.navigate()

    login.login(USERNAME, PASSWORD)

    home.add_backpack_to_cart()

    home.open_cart()

    product = cart.verify_product()

    assert "Backpack" in product