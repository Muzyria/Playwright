import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page


class TestToDo:
    def test_to_do(self, page: Page):
        page.goto("https://demo.playwright.dev/todomvc/#/")
        expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
        task_field = page.get_by_placeholder("What needs to be done?")
        expect(task_field).to_be_empty()
        task_field.press_sequentially("TASK TODO 1")
        task_field.press("Enter")
        # page.pause()
        task_field.press_sequentially("TASK TODO 2")
        task_field.press("Enter")

        task_list = page.locator('//ul[@class="todo-list"]')

        count_task_list = task_list.locator('//li[@data-testid="todo-item"]')
        expect(count_task_list).to_have_count(2)

        count_task_list.nth(0).get_by_role('checkbox').check()

        expect(count_task_list.nth(0)).to_have_class('completed')
        expect(count_task_list.nth(1)).not_to_have_class('completed')

        page.wait_for_timeout(2000)
        print("FINISH")

    def test_todo(self, page):
        page.goto('https://demo.playwright.dev/todomvc/#/')
        expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
        input_field = page.get_by_placeholder('What needs to be done?')
        expect(input_field).to_be_empty()
        input_field.fill("Закончить курс по playwright")
        input_field.press('Enter')
        input_field.fill("Добавить в резюме, что умею автоматизировать")
        input_field.press('Enter')
        todo_item = page.get_by_test_id('todo-item')
        expect(todo_item).to_have_count(2)
        todo_item.get_by_role('checkbox').nth(0).click()
        expect(todo_item.nth(0)).to_have_class('completed')
