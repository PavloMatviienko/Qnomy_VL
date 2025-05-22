from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: str) -> None:
        self.page.click(locator)

    def fill(self, locator: str, value: str) -> None:
        self.page.fill(locator, value)

    def is_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)

    def get_text(self, locator: str) -> str:
        return self.page.inner_text(locator)

    def is_disabled(self, locator: str) -> bool:
        return self.page.locator(locator).is_disabled()
