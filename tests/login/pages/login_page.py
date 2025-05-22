from playwright.sync_api import Page
from helps.fill_inputs import fill_inputs
from tests.common.base_page import BasePage
from tests.login.locators_login.login import PERSONAL_ID_FIELD, BIRTH_DATE_FIELD

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_button = page.get_by_role("button", name="Log in")
        self.checkbox = page.get_by_role("checkbox", name="I agree to Terms & Conditions")

    def fill_personal_id(self, personal_id: str) -> None:
        fill_inputs(input_id=PERSONAL_ID_FIELD, input_date=personal_id, page=self.page)

    def fill_birth_date(self, birth_date: str) -> None:
        fill_inputs(input_id=BIRTH_DATE_FIELD, input_date=birth_date, page=self.page)

    def click_checkbox(self) -> None:
        self.checkbox.click()

    def is_checkbox_checked(self) -> bool:
        return self.checkbox.is_checked()

    def is_login_button_disabled(self) -> bool:
        return self.login_button.is_disabled()

    def is_login_button_enabled(self) -> bool:
        return not self.login_button.is_disabled()