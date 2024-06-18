"""Inventory page"""
import re

from playwright.sync_api import Page

class InventoryPage:
    """Methods and properties for the Inventory page"""
    def __init__(self, page: Page) -> None:
        self.page = page

        # Locators
        self.menu = page.get_by_role("button", name=re.compile("open menu", re.IGNORECASE))
        self.menu_logout = page.locator("[data-test=\"logout-sidebar-link\"]")
        # XPATH is not the suggested way of locating the button.
        self.first_item_button = page.locator(
            "xpath=//div[@id='inventory_container']//button"
            ).first
        self.first_item_name = page.locator("div[class='inventory_item_name ']").first
        self.first_item_price = page.locator("div[class='inventory_item_price']").first
        self.cart_icon = page.locator("span[class='shopping_cart_badge']")

    def title(self) -> str:
        """Page title"""
        return self.page.title()

    def url(self) -> str:
        """Page URL"""
        return self.page.url

    def logout(self) -> None:
        """Login out from the app"""
        self.menu.click()
        self.menu_logout.click()


    def get_first_item_name(self) -> str:
        """Get the name of the firts item in the Inventory page"""
        return self.first_item_name.text_content()

    def get_first_item_price(self) -> str:
        """Get the price of the firts item in the Inventory page"""
        return self.first_item_price.text_content()

    def add_first_item_to_cart(self) -> None:
        """Add the firts item to the cart"""
        self.first_item_button.click()

    def get_first_item_button_text(self) -> str:
        """Get the text of the first item button in the Inventory page"""
        return self.first_item_button.text_content()

    def get_cart_icon_text(self) -> str:
        """Get the text from the cart icon"""
        return self.cart_icon.text_content()

    def click_cart_icon_text(self):
        """Go to the "Cart" page"""
        return self.cart_icon.click()
