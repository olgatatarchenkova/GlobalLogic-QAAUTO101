import pytest
from modules.api.clients import Github
from modules.ui.page_objects import CleanBrowserSession


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Olga"
        self.second_name = "Test"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = Github()
    yield api


@pytest.fixture
def browser_session():
    session = CleanBrowserSession()

    yield session

    session.close()
    session.quit()
