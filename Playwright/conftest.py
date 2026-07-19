import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        yield page
        page.close()