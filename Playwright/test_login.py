def test_lockedUser(page):
        page.locator("#user-name").fill("locked_out_user")
        page.locator("#password").fill("secret_sauc")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)
def test_problem_user(page):
        page.locator("#user-name").fill("problem_user")
        page.locator("#password").fill("secret_sauc")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)
def test_error_user(page):
        page.locator("#user-name").fill("error_user")
        page.locator("#password").fill("secret_sauc")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)

def test_Validlogin(page):
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        page.wait_for_timeout(5000)