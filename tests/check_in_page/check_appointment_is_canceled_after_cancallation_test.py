import re

import allure
import pytest
from playwright.sync_api import Page, expect
from config import VL_URL_WITH_PROCESS, PERSONAL_ID, BIRTH_DATE
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD,CHECK_BOX_FIELD


@pytest.mark.default_configuration
@allure.title('Сancel error page when appointment was reopened')
@allure.story('Customer opened the link with canceled appointment')
def test_appointment_canceled_page(page: Page) -> None:
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
    with allure.step('Check if appointment is canceled'):
        expect(page.get_by_role("heading")).to_contain_text("Appointment has been cancelled")

    screenshot_path = 'tests/check_in_page/screenshots/appointment_canceled_error_page.png'
    screenshot_bytes = page.screenshot(path=screenshot_path)
    allure.attach(
        screenshot_bytes,
        name='appointment_canceled_error_page',
        attachment_type=allure.attachment_type.PNG
    )