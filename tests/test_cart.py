"""Cart tests"""
from models.configuration import Configuration
from pages.cart import CartPage
from pages.inventory import InventoryPage
from pages.login import LoginPage


def test_add_to_cart(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    config: Configuration
    ) -> None:
    """Checking the logout feature"""
    # Step 1: Arrange (Login)
    login_page.navigate()
    login_page.login(config.user, config.password)
    assert inventory_page.url() == config.url + "/inventory.html"

    first_item_name: str = inventory_page.get_first_item_name()
    first_item_price: str = inventory_page.get_first_item_price()

    # Step 2: Act (Add the firs item to the cart)
    inventory_page.add_first_item_to_cart()
    assert "Remove" == inventory_page.get_first_item_button_text()
    assert "1" == inventory_page.get_cart_icon_text()

    # Step 3: Assert (Check the cart contains the selected item)
    inventory_page.click_cart_icon_text()
    assert cart_page.url() == config.url + "/cart.html"

    cart_item_name: str = cart_page.get_first_item_name()
    cart_item_price: str = cart_page.get_first_item_price()

    assert 1 == cart_page.get_number_of_items()
    assert first_item_name == cart_item_name
    assert first_item_price == cart_item_price
