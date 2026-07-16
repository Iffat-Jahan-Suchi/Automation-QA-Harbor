from playwright.sync_api import sync_playwright

def test_smoke():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        page.wait_for_timeout(3000)
        #list wise
        # buttons=page.locator("button:has-text('Add to cart')")
        # buttons.nth(0).click()
        # buttons.nth(1).click()
        # page.wait_for_timeout(5000)
        #raw wise
        products=page.locator(".inventory_item").all()
        products[0].locator("button:has-text('Add to cart')").click()
        products[1].locator("button:has-text('Add to cart')").click()
        page.locator(".shopping_cart_link").click()
        page.locator("#checkout").click()
        page.locator("#first-name").fill("iffat")
        page.locator("#last-name").fill("jahan")
        page.locator("#postal-code").fill("569874")
        page.locator("#continue").click()
        page.mouse.wheel(0, 1000)
        page.locator("#finish").click()
        page.locator("#back-to-products").click()
        page.locator("#react-burger-menu-btn").click()
        page.locator("#logout_sidebar_link").click()
        page.wait_for_timeout(3000)




