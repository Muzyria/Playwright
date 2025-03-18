import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page, Route



class TestApi:
    def test_mock_tags(self, page: Page):
        page.route("**/api/tags", lambda route: route.fulfill(path="test_api/data.json"))
        page.goto('https://demo.realworld.io/')
        page.wait_for_timeout(3000)

    def test_intercepted(self, page: Page):
        def handle_route(route: Route):
            response = route.fetch()
            json = {}
            json["tags"] = ["open", "solutions"]
            route.fulfill(json=json)

        page.route("**/api/tags", handle_route)

        page.goto("https://demo.realworld.io/")
        sidebar = page.locator('css=div.sidebar')
        expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])
        page.wait_for_timeout(3000)

    # def test_intercepted(self, page: Page):
    #     def handle_route(route: Route):
    #         response = route.fetch()
    #         json_data = response.json() if response.status == 200 and response.body() else {}
    #         json_data["tags"] = ["open", "solutions"]
    #
    #         route.fulfill(json=json_data)
    #
    #     page.route("**/api/tags", handle_route)
    #
    #     page.goto("https://demo.realworld.io/")
    #     page.wait_for_timeout(5000)
    #
    #     sidebar = page.locator("div.sidebar")
    #     expect(sidebar.get_by_role("link")).to_contain_text(["open", "solutions"])

    def test_inventory(self, page: Page):
        response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
        print(response.status)
        print(response.json())