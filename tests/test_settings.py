import pytest
import time
from tests.conftest import setup
from pages.Settings_admin import Settings_Page

@pytest.fixture
def test_login(setup):
    print("Login Successfully")
    time.sleep(4)

def test_Report(test_login,driver):
    settings_admin = Settings_Page(driver)
    settings_admin.open_settings(driver)