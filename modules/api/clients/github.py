import requests

class Github:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories",
                         params={"q": name})
        body = r.json()

        return body

    def list_stargazers(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/stargazers")
        body = r.json()

        return body

    def list_watchers(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/watchers")
        body = r.json()

        return body
