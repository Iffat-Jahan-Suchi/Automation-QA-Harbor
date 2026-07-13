from playwright.sync_api import sync_playwright

def test_lockedUser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        page.locator("#user-name").fill("locked_out_user")
        page.locator("#password").fill("secret_sauc")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)
def test_problem_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        page.locator("#user-name").fill("problem_user")
        page.locator("#password").fill("secret_sauc")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)
def test_error_user():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        page.locator("#user-name").fill("error_user")
        page.locator("#password").fill("secret_sauc")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)

def test_Validlogin():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)