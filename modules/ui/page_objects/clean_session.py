from selenium import webdriver

class CleanSession:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
