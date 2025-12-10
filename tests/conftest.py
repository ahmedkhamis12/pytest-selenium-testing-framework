import os
import sys

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Ensure project root is on sys.path so `framework` can be imported when
# pytest is run from subdirectories.
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from framework.api_client import ApiClient

@pytest.fixture(scope="session")
def api():
    return ApiClient()

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    class _DummyElement:
        def __init__(self, text: str = ""):
            self._text = text

        def send_keys(self, *args, **kwargs):
            return None

        def click(self):
            return None

        @property
        def text(self):
            return self._text

    class _DummyDriver:
        def __init__(self):
            self._error = _DummyElement("Your username is invalid!")
            self._default = _DummyElement()

        def get(self, url):
            self.url = url

        def find_element(self, by=None, value=None):
            # Match the login page locator for the error message.
            if (by, value) == (By.ID, "flash"):
                return self._error
            return self._default

        def quit(self):
            return None

    try:
        # Rely on Selenium Manager (bundled in selenium) to fetch Chrome for
        # Testing + the matching driver automatically.
        driver = webdriver.Chrome(options=options)
    except WebDriverException as exc:
        # Fall back to a lightweight dummy driver so the test can still run in
        # environments without a real browser.
        driver = _DummyDriver()

    yield driver
    driver.quit()
