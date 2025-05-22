import allure
import pytest
from playwright.sync_api import expect

from config import VL_URL_WITHOUT_PROCESS, PERSONAL_ID_WRONG, BIRTH_DATE_WRONG
from tests.common.checkin_login_page import CheckInLoginPage

@pytest.mark.default_configuration
@allure.title('Tests of the Login page - field highlights and login errors')
@allure.story('Check red highlight and login error scenarios')
@pytest.mark.parametrize(
    "scenario",
    [
        "birthdate_field_red_highlight",
        "personalid_field_red_highlight",
        "login_error_wrong_data"
    ]
)
def test_login_field_highlights_and_errors(page, get_screenshot, scenario: str):
    login_page = CheckInLoginPage(page)
    login_page.open(VL_URL_WITHOUT_PROCESS)

    if scenario == "birthdate_field_red_highlight":
        with allure.step('Select the Birthdate field'):
            page.click(f'input[id={login_page.birth_date_field}]')
        with allure.step('Tick the Checkbox'):
            login_page.click_checkbox()
        with allure.step('Check if the Birthdate field is highlighted in red'):
            border_color = page.eval_on_selector(f'input[id="{login_page.birth_date_field}"]', "el => getComputedStyle(el).borderColor")
            assert border_color == "rgb(169, 46, 38)", f"Expected red border but got {border_color}"
        with allure.step('Take screenshot of Birthdate field red highlight'):
            get_screenshot(
                filename='red_border_of_the_birthdate_field.png',
                allure_name='Red border of the Birthdate field',
                path='tests/login/screenshots'
            )

    elif scenario == "personalid_field_red_highlight":
        with allure.step('Select the PersonalId field'):
            page.click(f'input[id={login_page.personal_id_field}]')
        with allure.step('Tick the Checkbox'):
            login_page.click_checkbox()
        with allure.step('Check if the PersonalId field is highlighted in red'):
            border_color = page.eval_on_selector(f'input[id="{login_page.personal_id_field}"]', "el => getComputedStyle(el).borderColor")
            assert border_color == "rgb(169, 46, 38)", f"Expected red border but got {border_color}"
        with allure.step('Take screenshot of PersonalId field red highlight'):
            get_screenshot(
                filename='red_border_of_the_personalid_field.png',
                allure_name='Red border of the PersonalId field',
                path='tests/login/screenshots'
            )

    elif scenario == "login_error_wrong_data":
        with allure.step('Fill the PersonalId field by wrong Id'):
            login_page.fill_personal_id(PERSONAL_ID_WRONG)
        with allure.step('Fill the Birthdate field by wrong value'):
            login_page.fill_birth_date(BIRTH_DATE_WRONG)
        with allure.step('Tick the Checkbox'):
            login_page.click_checkbox()
        with allure.step('Press the submit button'):
            login_page.click_submit()
        with allure.step('Check if the Log in error message is displayed'):
            expect(login_page.get_login_error_element()).to_be_visible()
        with allure.step('Take screenshot of login error'):
            get_screenshot(
                filename='login_error.png',
                allure_name='Login error',
                path='tests/login/screenshots'
            )
