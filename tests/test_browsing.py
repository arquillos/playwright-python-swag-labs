"""Browsing tests"""

from models.configuration import Configuration
from pages.login import LoginPage

from pages.inventory import InventoryPage



def test_login(
    login_page: LoginPage, inventory_page: InventoryPage, config: Configuration
    ) -> None:
    """Checking the login feature"""
    # Step 1: Arrange
    login_page.navigate()
    assert login_page.url() == config.url + "/"
    assert login_page.title() == "Swag Labs"

    # Step 2: Act
    login_page.login(config.user, config.password)

    # Step 3: Assert
    assert inventory_page.url() == config.url + "/inventory.html"


def test_logout(
    login_page: LoginPage, inventory_page: InventoryPage, config: Configuration
    ) -> None:
    """Checking the logout feature"""
    # Step 1: Arrange
    login_page.navigate()
    login_page.login(config.user, config.password)
    assert inventory_page.url() == config.url + "/inventory.html"

    # Step 2: Act
    inventory_page.logout()

    # Step 3: Assert
    assert login_page.url() == config.url + "/"
