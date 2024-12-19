from selenium.webdriver.common.by import By


class LoginPage():
    URL = "https://github.com/login"

    def __init__(self, driver) -> None:
        self.driver = driver

    def go_to(self):
        self.driver.get(LoginPage.URL)

    def user_login(self, username, password):
        login_element = self.driver.find_element(By.ID, "login_field")
        login_element.send_keys(username)

        password_element = self.driver.find_element(By.ID, "password")
        password_element.send_keys(password)

        sign_in_button = self.driver.find_element(By.NAME, "commit")
        sign_in_button.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
