
from playwright.sync_api import Page, expect

from config import VL_URL, PERSONAL_ID, BIRTH_DATE
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD


def test_submit_button_not_eneabled(page: Page):
    page.goto(VL_URL)
    fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=PERSONAL_ID, page=page)
    fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=BIRTH_DATE, page=page )

    submit_button = page.locator('button[type="submit"]')
    expect(submit_button).to_be_disabled()
    assert not submit_button.is_enabled()
    page.screenshot(path='tests/login/screenshots/submit_disabled.png')
