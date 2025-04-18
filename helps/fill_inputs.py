from playwright.sync_api import Page


def fill_inputs(input_id: str, input_date: str, page: Page):
    page.fill(f'input[id="{input_id}"]', input_date)
