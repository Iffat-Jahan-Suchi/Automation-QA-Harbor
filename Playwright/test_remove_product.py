from test_assert import test_valid_login

def test_remove_product(page):
    test_valid_login(page)
    products = page.locator(".inventory_item").all()
    products[0].locator("button:has-text('Add to cart')").click()
    products[1].locator("button:has-text('Add to cart')").click()
    page.locator(".shopping_cart_link").click()
    assert page.locator(".cart_item").count() == 2
    page.wait_for_timeout(2000)
    page.locator("button:has-text('Remove')").nth(0).click()
    page.wait_for_timeout(2000)
    assert page.locator(".cart_item").count() == 1



