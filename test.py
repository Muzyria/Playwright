from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://beta.syncwise360.com/loginabout:blank")
    page.goto("https://beta.syncwise360.com/login")
    page.get_by_label("username").click()
    page.get_by_label("username").fill("QA")
    page.get_by_label("password").click()
    page.get_by_label("password").fill("Qwerty01!")
    page.get_by_label("submit").click()
    page.get_by_label("geofence").click()
    page.get_by_label("geofence").click()
    page.get_by_label("geofence").click()
    page.locator(".closeModal").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
