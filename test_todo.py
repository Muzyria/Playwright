import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_add_todo(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()


def test_login(page: Page):
    # page.on("request", lambda request: print(">>", request.method, request.url))
    #
    # page.route("**/UserAccountLogin/**", lambda route: route.continue_(post_data='{"username":"eighteendev","password":"Qwerty01!"}'))
    #
    # # Логируем ответ сервера
    # page.on("response", lambda response: print("<<",  response.json() if "UserAccountLogin" in response.url else None))

    # page.on("request", lambda request: print(">>", request.method, request.post_data))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    page.goto('https://sandbox2.syncwise360.com/login')

    # page.locator("//input[@id='username']").type("adminexamplecom")
    # page.locator("//input[@id='username']").clear()
    #
    # page.locator("//input[@id='username']").fill("adminexamplecom")
    # page.locator("//input[@id='username']").clear()

    page.locator("//input[@id='username']").fill("eighteendev")
    page.locator("//input[@id='password']").fill("Qwerty01!")
    element = page.locator('//button[@aria-label="submit"]')

    element.evaluate("(el) => el.textContent = 'Новый текст'")
    element.evaluate("(el) => el.style.backgroundColor = 'red'")

    # expect(element, "no text --------").to_have_text("Новый")

    # element.screenshot(path="screenshots/screenshot.png")
    element.click()
    print("PRESS BUTTON SUBMIT")

    page.locator('//button[@aria-label="profile-icon"]').click()
    print("PRESS BUTTON PROFILE")

    time.sleep(5)




def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()


def test_select(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")


def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")



def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", lambda dialog: print(dialog.message))
    page.get_by_text("Диалог Confirmation").click()


# def test_dialogs(page: Page):
#     page.goto("https://zimaev.github.io/dialog/")
#     # Создаем переменную для хранения сообщения
#     dialog_message = None
#     # Обработчик диалога
#     def handle_dialog(dialog):
#         nonlocal dialog_message  # Используем nonlocal для изменения переменной в замыкании
#         dialog_message = dialog.message
#         dialog.accept()
#     # Подписываемся на событие диалога
#     page.on("dialog", handle_dialog)
#     # Вызываем диалог
#     page.get_by_text("Диалог Confirmation").click()
#     # Выводим сообщение из диалога
#     print("Сообщение из диалога:", dialog_message)


def test_new_tab(page: Page):
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()


def test_open_two_tabs(page: Page) -> None:
    page1 = page
    page2 = page.context.new_page()

    page1.goto("https://zimaev.github.io/tabs/")

    page2.goto("https://zimaev.github.io/dialog/")

    page1.bring_to_front()
    assert page1.url == "https://zimaev.github.io/tabs/"
    page2.bring_to_front()
    assert page2.url == "https://zimaev.github.io/dialog/"
    time.sleep(5)


def test_capture_websocket_messages(page: Page):
    # Перехватываем события WebSocket
    def on_ws(ws):
        print(f"WebSocket открыт: {ws.url}")
        ws.on("framereceived", lambda frame: print(f"Получено: {frame}"))
        ws.on("framesent", lambda frame: print(f"Отправлено: {frame}"))

    page.on("websocket", on_ws)

    page.goto('https://sandbox2.syncwise360.com/login')

    # Заполняем форму и кликаем кнопку
    page.locator("//input[@id='username']").fill("eighteendev")
    page.locator("//input[@id='password']").fill("Qwerty01!")
    element = page.locator('//button[@aria-label="submit"]')

    element.click()
    print("Нажата кнопка submit")
    page.wait_for_timeout(30000)



