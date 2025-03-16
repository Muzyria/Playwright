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
    page.goto('https://sandbox2.syncwise360.com/login')

    # page.locator("//input[@id='username']").type("adminexamplecom")
    # page.locator("//input[@id='username']").clear()
    #
    # page.locator("//input[@id='username']").fill("adminexamplecom")
    # page.locator("//input[@id='username']").clear()

    page.locator("//input[@id='username']").fill("eighteendev")
    page.locator("//input[@id='password']").fill("Qwerty01!")
    element = page.locator('//button[@aria-label="submit"]')
    # element.screenshot(path="screenshots/screenshot.png")
    element.click()
    print("PRESS BUTTON SUBMIT")

    page.locator('//button[@aria-label="profile-icon"]').click(timeout=30000)
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
