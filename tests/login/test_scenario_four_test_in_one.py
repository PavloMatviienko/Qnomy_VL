import pytest
import allure
from playwright.sync_api import Page

from config import VL_URL_WITH_PROCESS, PERSONAL_ID, BIRTH_DATE
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD,CHECK_BOX_FIELD


@pytest.mark.default_configuration
@allure.title('')
@pytest.mark.parametrize(
    'scenario, locators, value_date',
    [
        ('login button, is disabled', None,None),
        ('enter personal id  and check login button is disabled', PERSONAL_ID_FIELD, PERSONAL_ID),
        ('enter birthday   and check login button is disabled', BIRTH_DATE_FIELD, BIRTH_DATE),
        ('click the checkbox', None, None)
    ]
)
def test_login_page(page: Page, scenario: str, locators: str, value_date: str, get_screenshot):
    with allure.step('Opening the virtual lobby url'):
        page.goto(VL_URL_WITH_PROCESS)

    if locators and value_date:
        fill_inputs(input_id=locators, input_date=value_date, page=page)
    if 'checkbox' in scenario:
        check_box = page.get_by_role("checkbox", name="I agree to Terms & Conditions")
        check_box.click()
        assert check_box.is_checked()
    elif locators and value_date is None:
        page.click(locators)

    login_button = page.get_by_role("button", name="Log in")
    with allure.step(f'[{scenario}] Assert login button is disabled'):
        assert login_button.is_disabled()

    with allure.step(f"Take a screenshot: {scenario}"):
        get_screenshot(
            filename=scenario.replace(" ", "_"),
            allure_name=scenario,
            path="tests/login/screenshots/"
        )

import pytest
import allure
from playwright.sync_api import Page

from config import VL_URL_WITH_PROCESS, PERSONAL_ID, BIRTH_DATE
from tests.login.pages.login_page import LoginPage

@pytest.mark.default_configuration
@allure.title('Login Page Validation Scenarios')
@pytest.mark.parametrize(
    'scenario, action',
    [
        ('login button is disabled by default', 'default'),
        ('enter personal ID only and check login button is disabled', 'personal_id'),
        ('enter birth date only and check login button is disabled', 'birth_date'),
        ('click the checkbox and check login button is disabled', 'checkbox')
    ]
)
def test_login_page(page: Page, scenario: str, action: str, get_screenshot):
    login_page = LoginPage(page)

    with allure.step("Open login page"):
        login_page.open(VL_URL_WITH_PROCESS)

    with allure.step(f"Execute action: {action}"):
        if action == 'personal_id':
            login_page.fill_personal_id(PERSONAL_ID)
        elif action == 'birth_date':
            login_page.fill_birth_date(BIRTH_DATE)
        elif action == 'checkbox':
            login_page.click_checkbox()
            assert login_page.is_checkbox_checked()
        # default — нічого не робимо

    with allure.step(f"[{scenario}] Assert login button is disabled"):
        assert login_page.is_login_button_disabled()

    with allure.step(f"Take a screenshot: {scenario}"):
        get_screenshot(
            filename=scenario.replace(" ", "_"),
            allure_name=scenario,
            path="tests/login/screenshots/"
        )
