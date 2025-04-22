from playwright.sync_api import Page, expect

from config import VL_URL, PERSONAL_ID_WRONG, BIRTH_DATE_WRONG
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD


def test_login_error(page:Page):
    page.goto(VL_URL)
    fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=PERSONAL_ID_WRONG, page=page)
    fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=BIRTH_DATE_WRONG, page=page)

    page.click('input[type="checkbox"]')
    page.click('button[type="submit"]')

    expect(page.get_by_text("Log in error")).to_be_visible()

    #error_message = page.get_by_text('Log in error')
    
    page.screenshot(path='tests/login/screenshots/login_error.png')