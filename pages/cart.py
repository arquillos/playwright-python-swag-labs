"""Cart page"""
import logging

from playwright.sync_api import Page

class CartPage:
    """Methods and properties for the Cart page"""
    def __init__(self, page: Page) -> None:
        self.page = page

        # Locators
        self.cart_items = page.locator("div[class='cart_item']")
        self.cart_first_item_name = page.locator("div[class='inventory_item_name']").first
        self.cart_first_item_price = page.locator("div[class='inventory_item_price']").first

    def title(self) -> str:
        """Page title"""
        return self.page.title()

    def url(self) -> str:
        """Page URL"""
        # Unuseful logging call. Used to test the loggin configuration
        logging.debug("Cart page URL: %s", self.page.url)
        return self.page.url

    def get_number_of_items(self) -> int:
        """Get the number of elements in the cart"""
        return self.cart_items.count()

    def get_first_item_name(self) -> str:
        """Get the name of the first element in the cart"""
        return self.cart_first_item_name.text_content()

    def get_first_item_price(self) -> str:
        """Get the price of the first element in the cart"""
        return self.cart_first_item_price.text_content()
