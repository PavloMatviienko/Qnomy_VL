import allure
import pytest
from playwright.sync_api import Page, expect

from config import VL_URL_WITHOUT_PROCESS
from tests.login.locators_login.login import PERSONAL_ID_FIELD, CHECK_BOX_FIELD


@pytest.mark.default_configuration
@allure.title('Tests of the Login page')
@allure.story('Red highlight of the Personalid field when it selected but not filled')
def test_personal_id_field_is_red(page : Page):
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITHOUT_PROCESS)
    with allure.step('Select the PersonalId field'):
        page.click(f'input[id={PERSONAL_ID_FIELD}]')
    with allure.step('Tick the Checkbox'):
        page.click(f'input[type={CHECK_BOX_FIELD}]')
    with allure.step('Check if the PersonalId field is highlighted'):
        personal_id_border = page.eval_on_selector('input[id="PersonalId"]', "el => getComputedStyle(el).borderColor")
        print(personal_id_border)
        assert personal_id_border == "rgb(169, 46, 38)"
    red_border_screenshot = page.screenshot(path='tests/login/screenshots/red_border_of_the_personalid_field.png')
    allure.attach(
        red_border_screenshot,
        name='red_border_of_the_personalid_field',
        attachment_type=allure.attachment_type.PNG
    )
