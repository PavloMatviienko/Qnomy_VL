from playwright.sync_api import Page, expect

from config import VL_URL
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD


def test_birthdate_field_is_red(page : Page):
    page.goto(VL_URL)
    page.click('input[id="birthDate"]')
    page.click('input[type="checkbox"]')

    birthdate_border = page.eval_on_selector('input[id="birthDate"]', "el => getComputedStyle(el).borderColor")
    assert birthdate_border in ["rgb(169, 46, 38)", "red"]

    page.screenshot(path='tests/login/screenshots/red_border_of_the_birthdate_field.png')