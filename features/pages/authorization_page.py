from selenium.webdriver.chrome.webdriver import WebDriver

class AuthorizationPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def name_field(self):
        return self.driver.find_element_by_id('name')

    def title_field(self):
        return self.driver.find_element_by_id('title')

    def submit_button(self):
        return self.driver.find_element_by_id('authorizeButton')

