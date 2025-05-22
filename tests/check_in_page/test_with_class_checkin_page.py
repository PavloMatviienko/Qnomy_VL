import allure
import pytest
from playwright.sync_api import Page

from config import VL_URL_WITH_PROCESS, PERSONAL_ID, BIRTH_DATE
from tests.common.checkin_login_page import CheckInLoginPage

@pytest.mark.default_configuration
@allure.title('Customer log in to the appointment')
@allure.story('Checkin page is shown when login is correct')
def test_login_to_checkin(page: Page, get_screenshot):
    login_page = CheckInLoginPage(page)

    with allure.step('Open Virtual Lobby'):
        login_page.open(VL_URL_WITH_PROCESS)

    with allure.step('Fill Personal ID'):
        login_page.fill_personal_id(PERSONAL_ID)

    with allure.step('Fill Birth Date'):
        login_page.fill_birth_date(BIRTH_DATE)

    with allure.step('Click the checkbox'):
        login_page.click_checkbox()

    with allure.step('Click Submit'):
        login_page.click_submit()

    with allure.step('Wait for check-in page'):
        login_page.wait_for_checkin_page()

    with allure.step('Assert welcome message is visible'):
        assert login_page.get_welcome_message_element().is_visible()

    with allure.step('Take screenshot of the check-in page'):
        get_screenshot(
            filename="checkin_page",
            allure_name="Check-in screen",
            path="tests/check_in_page/screenshots"
        )
