import re

import allure
import pytest
from playwright.sync_api import Page, expect
from config import VL_URL_WITH_PROCESS, PERSONAL_ID, BIRTH_DATE
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD,CHECK_BOX_FIELD


@pytest.mark.default_configuration
@allure.title('Сancel appointment in the Checkin page')
@allure.story('Customer cancel appointment with choosing the reason')
def test_cancel_appointment(page: Page) -> None:
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITH_PROCESS)
    with allure.step('Fill the PersonalId field by wrong Id'):
        fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=PERSONAL_ID, page=page)
    with allure.step('Select the Birthdate field'):
        fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=BIRTH_DATE, page=page)
    with allure.step('Tick the Checkbox'):
        page.click(f'input[type={CHECK_BOX_FIELD}]')
    with allure.step('Tick the Submit button'):
        page.get_by_role("button", name="Log in").click()
    with allure.step('Press cancel button'):
        page.get_by_role("button", name="Cancel").click()
    page.get_by_role("combobox").click()
    with allure.step('Choose the reason'):
        page.get_by_role("option", name="Late").click()
    with allure.step('Confirm the cancellation'):
        page.get_by_role("button", name="Cancel appointment").click()
    with allure.step('Check if appointment is canceled'):
        expect(page.get_by_role("heading")).to_contain_text("Appointment has been cancelled")

    screenshot_path = 'tests/check_in_page/screenshots/appointment_canceled.png'
    screenshot_bytes = page.screenshot(path=screenshot_path)
    allure.attach(
        screenshot_bytes,
        name='appointment_canceled',
        attachment_type=allure.attachment_type.PNG
    )
