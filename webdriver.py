from selenium import webdriver
import os

class Driver:

    def __init__(self):
        # self.instance = webdriver.Chrome()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.instance = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")