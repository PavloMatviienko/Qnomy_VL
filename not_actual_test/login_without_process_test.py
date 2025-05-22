import re

import allure
import pytest
from playwright.sync_api import Page, expect
from config import VL_URL_WITHOUT_PROCESS, PERSONAL_ID, BIRTH_DATE
from helps.fill_inputs import fill_inputs
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD, CHECK_BOX_FIELD


@pytest.mark.default_configuration
@allure.title('Login without Process Guid to Personal Area Page')
@allure.story('Login to the Personal Area page when process guid is absent')
def test_fill_form(page: Page, get_screenshot):  # Додаємо фікстуру get_screenshot
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITHOUT_PROCESS)

    with allure.step('Fill the PersonalId field by wrong Id'):
        fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=PERSONAL_ID, page=page)

    with allure.step('Select the Birthdate field'):
        fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=BIRTH_DATE, page=page)

    with allure.step('Tick the Checkbox'):
        page.click(f'input[type={CHECK_BOX_FIELD}]')

    with allure.step('Press the button submit'):
        page.click('button[type="submit"]')

    with allure.step('Check if the Personal Area page is opened'):
        expect(page).to_have_url(re.compile('.*personal-area-page.*'))

    welcome_message = page.get_by_text('area')
    assert welcome_message.is_visible()

    with allure.step('Take a screenshot of the Personal Area Page'):
        get_screenshot(filename='personal_area', allure_name='Personal Area Page', path='tests/login/screenshots/')  # Використовуємо фікстуру
