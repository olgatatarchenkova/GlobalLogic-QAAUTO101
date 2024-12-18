import pytest

@pytest.mark.api
def test_user_exists(github_api):
    github_user = github_api.get_user('defunkt')
    assert github_user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    response = github_api.get_user('butenkosergii')
    # print(response)
    assert response['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    response = github_api.search_repo("become-qa-auto")
    # print(response)
    assert response['total_count'] == 58


@pytest.mark.api
def test_repo_cannnot_be_found(github_api):
    response = github_api.search_repo("sergiibutenko_repo_non_exist")
    # print(response)
    assert response['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    response = github_api.search_repo("s")
    # print(response)
    assert response['total_count'] != 0


@pytest.mark.api
def test_user_repo_is_starred(github_api):
    response = github_api.list_stargazers('BMayhew', 'awesome-sites-to-test-on')
    # print(response)
    assert response != []


@pytest.mark.api
def test_user_repo_is_not_starred(github_api):
    response = github_api.list_stargazers('olgatatarchenkova', 'disappearing-text-app')
    # print(response)
    assert response == []


@pytest.mark.api
def test_user_repo_has_watchers(github_api):
    response = github_api.list_watchers('BMayhew', 'awesome-sites-to-test-on')
    print(response)
    assert response != []


@pytest.mark.api
def test_user_repo_has_no_watchers(github_api):
    response = github_api.list_watchers('olgatatarchenkova', 'disappearing-text-app')
    # print(response)
    assert response == []
