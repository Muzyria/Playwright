from playwright.sync_api import Page, Route, expect


class TestApiSyncwise:
    def test_mock_api(self, page: Page):
        print()
        def handle_route(route: Route):
            response = route.fetch()
            # json_data = response.json()  # Декодируем JSON
            print("JSON____")
            # print(json_data)
            # route.fulfill(json=json_data)  # Отдаем тот же JSON обратно
            route.fulfill(path="test_api/data_syncwice.json")  # Отдаем тот же JSON обратно

        # page.route("**/CartDetailsList/**", lambda route: route.fulfill(path="test_api/data_syncwice.json"))
        page.route("**/CartDetailsList/**", handle_route)

        page.goto('https://sandbox2.syncwise360.com/login')

        page.locator("//input[@id='username']").fill("eighteendev")
        page.locator("//input[@id='password']").fill("Qwerty01!")
        page.click('//button[@aria-label="submit"]')

        # page.wait_for_timeout(5000)

        page.click('//button[@routerlink="/asset"]')
        page.wait_for_timeout(5000)
