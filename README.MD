# Playwright with Python example

The goal of this repository is to create a minimal POM framework with Python and Playwright.

The tests will browse to the "Swag Labs" testing website (https://www.saucedemo.com/) and will test two workflows:
- Login
- Adding an element to the cart



## Installation
    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt

## Test execution
    .\.venv\Scripts\activate
    python -m pytest .\tests --headed --slowmo 1000 --screenshot only-on-failure
