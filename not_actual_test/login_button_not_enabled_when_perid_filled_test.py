import allure
import pytest
from playwright.sync_api import Page, expect

from config import VL_URL_WITHOUT_PROCESS, PERSONAL_ID, BIRTH_DATE
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD


@pytest.mark.default_configuration
@allure.title('Login button is disabled when fields are filled but checkbox not ticked')
@allure.story('Login Error when PersonalId and Birthdate are wrong')
def test_submit_button_disabled(page: Page):
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITHOUT_PROCESS)
    with allure.step('Fill the PersonalId field by valid data'):
        fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=PERSONAL_ID, page=page)
    with allure.step('Fill the Birthdate field by valid value'):
        fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=BIRTH_DATE, page=page )
    with allure.step('try to press button submit'):
        submit_button = page.locator('button[type="submit"]')
    expect(submit_button).to_be_disabled()
    assert not submit_button.is_enabled()

    screenshot_path = 'tests/login/screenshots/submit_disabled.png'
    screenshot_bytes = page.screenshot(path=screenshot_path)
    allure.attach(
        screenshot_bytes,
        name='submit_disabled',
        attachment_type=allure.attachment_type.PNG
    )