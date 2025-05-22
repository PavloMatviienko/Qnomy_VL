# tests/conftest.py
import os
import time

import pytest
import allure
from playwright.sync_api import Page
from datetime import datetime


@pytest.fixture
def get_screenshot(page: Page):
    def _get_screenshot(filename: str, allure_name: str, path: str):
        date_now = datetime.now().strftime('%Y-%m-%d_%H-%M')
        file_name = f'{date_now}_{filename}.png'
        full_path = os.path.join(path, file_name)
        screenshot_bytes = page.screenshot(path=full_path)
        print(f"Шлях до скріншоту: {full_path}")
        allure.attach(
            screenshot_bytes,
            name=allure_name,
            attachment_type=allure.attachment_type.PNG
        )

    return _get_screenshot


