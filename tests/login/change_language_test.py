import pytest
import allure
from playwright.sync_api import Page
from config import VL_URL_WITHOUT_PROCESS


@pytest.mark.test_with_language_selector
@allure.feature('Tests of the Login page')
@allure.story('Customer can change the language on the Login page')
def test_press_language_selector(page:Page):
    with allure.step('Opening url of the Virtual Lobby page'):
        page.goto(VL_URL_WITHOUT_PROCESS)
    with allure.step('Click to the language selector'):
        page.click(".ng-select-container")
        page.wait_for_selector(".ng-dropdown-panel")
    with allure.step('Change Hebrew language '):
        get_text_he = page.get_by_text("He")
        get_text_he.nth(1).click()
    with allure.step('Click to the language selector'):
        page.click(".ng-select-container")
    with allure.step('Check if Hebrew text is displayed'):
        welcome_message = page.get_by_text('שלום')
    assert welcome_message.is_visible()
    #page.screenshot(path='tests/login/screenshots/RTL_view.png')
    screenshot_path = 'tests/login/screenshots/RTL_view.png'
    screenshot_bytes = page.screenshot(path=screenshot_path)
    allure.attach(
        screenshot_bytes,
        name='RTL_view',
        attachment_type=allure.attachment_type.PNG
    )

