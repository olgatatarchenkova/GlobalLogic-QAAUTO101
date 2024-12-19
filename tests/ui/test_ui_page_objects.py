import pytest
from modules.ui.page_objects import LoginPage


@pytest.mark.ui
def test_check_incorrect_username_page_objects(browser_session):
    login_page = LoginPage(browser_session.driver)

    login_page.go_to()

    login_page.user_login("test@test.com", "wrong_password")

    assert login_page.check_title("Sign in to GitHub · GitHub")
