import allure
import pytest
from playwright.sync_api import Page, expect

from config import VL_URL_WITHOUT_PROCESS
from tests.login.locators_login.login import BIRTH_DATE_FIELD, CHECK_BOX_FIELD


@pytest.mark.default_configuration
@allure.title('Tests of the Login page')
@allure.story('Red highlight of the Birthdate field when it selected but not filled')
def test_birthdate_field_is_red(page : Page):
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITHOUT_PROCESS)
    with allure.step('Select the Birthdate field'):
        page.click(f'input[id={BIRTH_DATE_FIELD}]')
    with allure.step('Tick the Checkbox'):
        page.click(f'input[type={CHECK_BOX_FIELD}]')
    with allure.step('Check if the Birhdate field is highlighted'):
        birthdate_border = page.eval_on_selector('input[id="birthDate"]', "el => getComputedStyle(el).borderColor")
    assert birthdate_border == "rgb(169, 46, 38)"
    red_border_screenshot = page.screenshot(path='tests/login/screenshots/red_border_of_the_birthdate_field.png')
    allure.attach(
        red_border_screenshot,
        name='red_border_of_the_birthdate_field',
        attachment_type=allure.attachment_type.PNG
    )