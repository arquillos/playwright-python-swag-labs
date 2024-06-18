"""Test fixtures"""
import os
import pytest

from dotenv import load_dotenv
from playwright.sync_api import Page

from models.configuration import Configuration
from pages.cart import CartPage
from pages.login import LoginPage
from pages.inventory import InventoryPage


@pytest.fixture(scope="session")
def config() -> Configuration:
    """Get the credentials from the environment"""
    load_dotenv()
    return Configuration(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        url=os.getenv("BASE_URL")
    )


@pytest.fixture
def login_page(page: Page, config: Configuration) -> LoginPage:
    """Create the Login page object"""
    return LoginPage(page, config.url)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Create the Inventory page object"""
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Create the Cart page object"""
    return CartPage(page)
