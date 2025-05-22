import re

import allure
import pytest
from playwright.sync_api import Page, expect
from config import VL_URL_WITH_PROCESS, PERSONAL_ID, BIRTH_DATE
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD,CHECK_BOX_FIELD


@pytest.mark.test_with_language_selector
@allure.feature('Tests of the Checkin page')
@allure.story('Customer can change the language on the Checkin page')
def test_press_language_selector_in_checkin_page(page:Page):
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITH_PROCESS)
    with allure.step('Fill the PersonalId field by valid data'):
        fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=PERSONAL_ID, page=page)
    with allure.step('Fill the Birthdate field by valid value'):
        fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=BIRTH_DATE, page=page)
    with allure.step('Tick the Checkbox'):
        page.click(f'input[type={CHECK_BOX_FIELD}]')
    with allure.step('try to press button submit'):
        page.click('button[type="submit"]')
    with allure.step('customer in the checkin page'):
     expect(page).to_have_url(re.compile(".*check-in.*"))
    with allure.step('Click to the language selector'):
        page.click(".ng-select-container")
        page.wait_for_selector(".ng-dropdown-panel")
    with allure.step('Change Hebrew language '):
        get_text_he = page.get_by_text("He")
        get_text_he.nth(1).click()
        page.click(".ng-select-container")
    with allure.step('Check if Hebrew text is displayed'):
        welcome_message = page.get_by_text('שלום')
    assert welcome_message.is_visible()
    screenshot_path = 'tests/check_in_page/screenshots/RTL_view_on_Checkin.png'
    screenshot_bytes = page.screenshot(path=screenshot_path)
    allure.attach(
        screenshot_bytes,
        name='RTL_view_on_Checkin',
        attachment_type=allure.attachment_type.PNG
    )