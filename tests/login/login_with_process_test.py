import re
from playwright.sync_api import Page, expect


def fill_form_test(page:Page):
    page.goto('https://qfinterfaces.qnomy.com:10443/QfRougeQa/VLv4.0.0/VLv4_mainQ64/#/start/PauloBank')
    page.fill('input[id="PersonalId"]', '000000093')
    page.fill('input[id="birthDate"]', '1992')
    page.click('input[type="checkbox"]')
    page.click('button[type="submit"]')
    # not finished