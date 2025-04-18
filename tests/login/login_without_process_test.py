import re
from playwright.sync_api import Page, expect


def test_fill_form(page:Page):
    page.goto('https://qfinterfaces.qnomy.com:10443/QfRougeQa/VLv4.0.0/VLv4_mainQ64/#/start/PauloBank')
    page.fill('input[id="PersonalId"]', '000000093')
    page.fill('input[id="birthDate"]', '1992')
    page.click('input[type="checkbox"]')
    page.click('button[type="submit"]')

    expect(page).to_have_url(re.compile('.*personal-area.*'))

    welcome_message = page.get_by_text('area')
    assert welcome_message.is_visible()
    page.screenshot(path='tests/login/screenshots/personal_area.png')




