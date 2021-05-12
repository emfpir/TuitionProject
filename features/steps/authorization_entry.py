from behave import given, when, then
from features.pages.authorization_page import AuthorizationPage
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep



@given('The User is on the Authorization Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get('file:///C:/Users/D/Documents/Revature/revature%20training/Project1/authorization.html')


@when('The User types {name} in the Name Field')
def step_impl(context, name):
    authorization_page: AuthorizationPage = context.authorization_page_open
    authorization_page.name_field().send_keys(name)


@when('The User types {title} in the Title Field')
def step_impl(context, title):
    authorization_page: AuthorizationPage = context.authorization_page_open
    authorization_page.title_field().send_keys(title)

@when('The User clicks the Submit Button')
def step_impl(context):
    authorization_page: AuthorizationPage = context.authorization_page_open
    authorization_page.submit_button().click()
    sleep(2)

@then('The banner should be {banner}')
def step_impl(context, banner):
    driver: WebDriver = context.driver
    assert driver.title == banner


#in terminal type:>behave -i authorization.feature



