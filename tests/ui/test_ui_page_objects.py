from modules.ui.page_objects import LoginPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_objects():
    login_page = LoginPage()

    login_page.go_to()

    login_page.user_login("test@test.com", "wrong_password")

    assert login_page.check_title("Sign in to GitHub · GitHub")
