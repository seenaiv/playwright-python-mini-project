from pages.login_page import LoginPage
from data.test_data import *

def test_login(page):

    login = LoginPage(page)
    login.navigate()

    login.login(USERNAME, PASSWORD)

    assert "inventory" in page.url

