import pytest
from playwright.sync_api import Playwright, sync_playwright, expect



# def pytest_fixture_setup(fixturedef, request):
#     print(f"Фикстура {fixturedef.scope} для {fixturedef.name} запускается")


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }
#     }


# @pytest.fixture
# def browser_fixture():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()

def browser_fixture():
    print("Запускается фикстура browser_fixture")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.is_fixture_active = True  # Добавляем атрибут для проверки
        yield page
        page.close()
        browser.close()
    print("Завершается фикстура browser_fixture")