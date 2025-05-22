import allure
import pytest
from playwright.sync_api import Page, expect

from config import VL_URL_WITHOUT_PROCESS, PERSONAL_ID_WRONG, BIRTH_DATE_WRONG
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD,CHECK_BOX_FIELD


@pytest.mark.default_configuration
@allure.title('Wrong data to login')
@allure.story('Login Error when PersonalId and Birthdate are wrong')
def test_login_error(page:Page):
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITHOUT_PROCESS)
    with allure.step('Fill the PersonalId field by wrong Id'):
        fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=PERSONAL_ID_WRONG, page=page)
    with allure.step('Fill the Birthdate field by wrong value'):
        fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=BIRTH_DATE_WRONG, page=page)
    with allure.step('Tick the Checkbox'):
        page.click(f'input[type={CHECK_BOX_FIELD}]')
    with allure.step('press the button submit'):
        page.click('button[type="submit"]')
    with allure.step('Check the if the Log in error message is displayed when data is wrong'):
         expect(page.get_by_text("Log in error")).to_be_visible()

    screenshot_path = 'tests/login/screenshots/login_error.png'
    screenshot_bytes = page.screenshot(path=screenshot_path)
    allure.attach(
        screenshot_bytes,
        name='login_error',
        attachment_type=allure.attachment_type.PNG
    )

