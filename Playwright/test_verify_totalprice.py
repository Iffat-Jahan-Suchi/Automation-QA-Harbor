from playwright.sync_api import sync_playwright
def login_locator(page,name,password):
    page.locator("#user-name").fill(name)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

def test_verifyTotalPrice(page):
        login_locator(page,"standard_user","secret_sauce")
        page.wait_for_timeout(2000)
        products=page.locator(".inventory_item")
        page.wait_for_timeout(2000)
        expectedPrice=0
        count=2
        for i in range(count):
            product = products.nth(i)
            price = product.locator(".inventory_item_price").text_content()
            expectedPrice += float(price.replace("$", ""))
            product.locator("button").click()
            page.wait_for_timeout(2000)

        page.locator(".shopping_cart_link").click()
        page.wait_for_timeout(2000)
        page.locator("#checkout").click()
        page.wait_for_timeout(2000)

        page.locator("#first-name").fill("iffat")
        page.locator("#last-name").fill("jahan")
        page.locator("#postal-code").fill("569874")
        page.locator("#continue").click()
        actualPrice = page.locator(".summary_subtotal_label").text_content()
        actualPrice = float(
            actualPrice.replace("Item total: $", "")
        )
        assert actualPrice == expectedPrice
        page.locator("#finish").click()
        page.wait_for_timeout(2000)
        page.locator("#back-to-products").click()
        page.wait_for_timeout(2000)
        page.locator("#react-burger-menu-btn").click()
        page.wait_for_timeout(2000)
        page.locator("#logout_sidebar_link").click()

