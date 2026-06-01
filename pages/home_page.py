class HomePage:

    def __init__(self,page):
        self.page= page

    def add_backpack_to_cart(self):

        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def open_cart(self):

        self.page.locator('.shopping_cart_link').click()