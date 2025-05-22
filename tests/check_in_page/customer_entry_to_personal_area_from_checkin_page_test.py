import allure
import pytest
from playwright.sync_api import Page

from config import VL_URL_WITH_PROCESS, PERSONAL_ID, BIRTH_DATE
from tests.common.checkin_login_page import CheckInLoginPage

@pytest.mark.default_configuration
@allure.title('Customer log in to the Personal area Page')
@allure.story('Personal Area Page is opened')
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

    with allure.step('Go to personal area'):
        login_page.go_to_personal_area()
    with allure.step('Assert Personal Area is visible'):
        assert login_page.get_welcome_personal_area_element().is_visible()

    with allure.step('Take screenshot of the personal are page'):
        get_screenshot(
            filename="personal_area_page",
            allure_name="Entry screen to personal area page",
            path="tests/check_in_page/screenshots"
        )