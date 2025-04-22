from playwright.sync_api import Page, expect

from config import VL_URL
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD


def test_personalid_field_is_red(page : Page):
    page.goto(VL_URL)
    page.click('input[id="PersonalId"]')
    page.click('input[type="checkbox"]')

    personal_id_border = page.eval_on_selector('input[id="PersonalId"]', "el => getComputedStyle(el).borderColor")
    assert personal_id_border in ["rgb(169, 46, 38)", "red"]

    page.screenshot(path='tests/login/screenshots/red_border_of_the_personalid_field.png')