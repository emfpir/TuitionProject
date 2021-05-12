from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from features.pages.authorization_page import AuthorizationPage

#All setup and teardown functions must go in this file
# These functions must be named using behave 's conventions
def before_all(context):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver: WebDriver = webdriver.Chrome('C:/Users/D/Documents/chromedriver_win32/chromedriver.exe', chrome_options = options )
    authorization_page_open = AuthorizationPage(driver)

    context.driver: WebDriver = driver
    context.authorization_page_open = authorization_page_open

def after_all(context):
    context.driver.quit()

    ##in terminal : type 'behave' to test