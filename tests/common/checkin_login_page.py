import re
from playwright.sync_api import Page, expect
from helps.fill_inputs import fill_inputs
from tests.common.base_page import BasePage
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD, CHECK_BOX_FIELD


class CheckInLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.personal_id_field = PERSONAL_ID_FIELD
        self.birth_date_field = BIRTH_DATE_FIELD
        self.checkbox_locator = f'input[type={CHECK_BOX_FIELD}]'
        self.submit_button = 'button[type="submit"]'

    def open(self, url: str) -> None:
        self.page.goto(url)

    def fill_personal_id(self, value: str) -> None:
        fill_inputs(input_id=self.personal_id_field, input_date=value, page=self.page)

    def fill_birth_date(self, value: str) -> None:
        fill_inputs(input_id=self.birth_date_field, input_date=value, page=self.page)

    def click_checkbox(self) -> None:
        self.page.click(self.checkbox_locator)

    def click_submit(self) -> None:
        self.page.click(self.submit_button)

    def wait_for_checkin_page(self) -> None:
        expect(self.page).to_have_url(re.compile(".*check-in.*"))

    def get_welcome_message_element(self):
        return self.page.get_by_text("upcoming meeting")

    def go_to_personal_area(self):
        self.page.get_by_role("button", name="Go to Personal Area").click()
    def get_welcome_personal_area_element(self):
        return self.page.locator("text=Welcome to your personal area")
    def get_login_error_element(self):
        return self.page.locator("text= Error")

    def take_screenshot(self, path: str) -> bytes:
        return self.page.screenshot(path=path)
