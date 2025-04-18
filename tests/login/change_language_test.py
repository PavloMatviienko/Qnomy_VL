import re
from playwright.sync_api import Page, expect


def test_press_language_selector(page:Page):
    page.goto('https://qfinterfaces.qnomy.com:10443/QfRougeQa/VLv4.0.0/VLv4_mainQ64/#/start/PauloBank')

    # Клік по контейнеру вибору мови (в головному page)
    page.click(".ng-select-container")
    page.wait_for_selector(".ng-dropdown-panel")
    get_text_he = page.get_by_text("He")
    get_text_he.nth(1).click()

    # Клік по контейнеру вибору мови (в головному page знову)
    page.click(".ng-select-container")
    #перевірка, чи ми на тій сторінці чи ні
    welcome_message = page.get_by_text('שלום')
    assert welcome_message.is_visible()


    page.screenshot(path='tests/login/screenshots/RTL_view.png')


