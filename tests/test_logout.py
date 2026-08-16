import time
import pytest
from tests.conftest import setup
from pages.logout import LogoutPage


@pytest.fixture
def test_login(setup):
     print("test_login")
     time.sleep(4)


def test_logout(test_login,driver):
       print("test_logout")
       logout_page = LogoutPage(driver)
       logout_page.open_logout()
       time.sleep(3)