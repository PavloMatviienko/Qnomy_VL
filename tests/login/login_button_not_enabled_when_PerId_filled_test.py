import re
from playwright.sync_api import Page, expect


def test_sumbit_button_not_enbled(page:Page):
    page.goto('https://qfinterfaces.qnomy.com:10443/QfRougeQa/VLv4.0.0/VLv4_mainQ64/#/start/PauloBank')
    page.fill('input[id="PersonalId"]', '000000093')
   # page.fill('input[id="birthDate"]', '1992')
    #page.click('input[type="checkbox"]')

    submit_button = page.locator('button[type="submit"]')
    expect(submit_button).to_be_disabled()
    assert not submit_button.is_enabled()
    page.screenshot(path='tests/login/screenshots/submit_disabled.png')
