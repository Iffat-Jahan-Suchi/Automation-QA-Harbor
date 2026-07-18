
from playwright.sync_api import sync_playwright, expect


def login_locator(page,username,password):
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

def test_valid_login():
 with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
    login_locator(page,"standard_user","secret_sauce")
    page.wait_for_timeout(5000)
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_userName():
 with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
    login_locator(page,"standard_users","secret_sauce")
    #page.wait_for_timeout(5000)
    error=page.locator("//h3[@data-test='error']")
    assert error.text_content() == "Epic sadface: Username and password do not match any user in this service"

def test_invalid_password():
 with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
    login_locator(page,"standard_user","secret_saucee")
    #page.wait_for_timeout(5000)
    error=page.locator("//h3[@data-test='error']")
    assert error.text_content() == "Epic sadface: Username and password do not match any user in this service"

def test_sortName():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        login_locator(page, "standard_user", "secret_sauce")
        page.locator(".product_sort_container").click()
        page.wait_for_timeout(5000)
        page.locator(".product_sort_container").select_option("za")
        names=page.locator(".product_sort_container").all_text_contents()
        assert names==sorted(names,reverse=True)
def test_priceLowToHigh():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        login_locator(page, "standard_user", "secret_sauce")
        page.locator(".product_sort_container").click()
        page.locator(".product_sort_container").select_option("lohi")
        expect(page.locator(".product_sort_container")).to_have_value("lohi")
def test_priceHighToLow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        login_locator(page, "standard_user", "secret_sauce")
        page.locator(".product_sort_container").click()
        page.locator(".product_sort_container").select_option("hilo")
        expect(page.locator(".product_sort_container")).to_have_value("hilo")



def test_cartItem():
 with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
    login_locator(page,"standard_user","secret_sauce")
    page.wait_for_timeout(3000)
    products=page.locator(".inventory_item")
    actualProducts=[]
    count=2
    for i in range(count):
        product=products.nth(i)
        name = product.locator(".inventory_item_name").text_content()
        price = product.locator(".inventory_item_price").text_content()
        actualProducts.append({
            "name":name,
            "price":price
        })
        product.locator("button:has-text('Add to cart')").click()

        page.wait_for_timeout(3000)
    cartCount=int(page.locator(".shopping_cart_link").text_content())
    assert cartCount==count
    page.locator("#shopping_cart_container").click()
    cart_items = page.locator(".cart_item")
    for i in range(count):
        expected_name = cart_items.nth(i).locator(".inventory_item_name").text_content()
        expected_price = cart_items.nth(i).locator(".inventory_item_price").text_content()
    assert expected_name==actualProducts[i]["name"]
    assert expected_price==actualProducts[i]["price"]

