from selenium import webdriver
import pytest


# baseline setup for unit test marked as fixture
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser.........")
    else:
        driver = webdriver.Ie()
        print("Launching Internet Explorer.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# HTML Report Configuration

# It is pre-define hooked for Adding Environment info to HTML Report

def pytest_metadata(metadata):
    metadata['Project Name'] = 'Developer Portal'
    metadata['Module Name'] = 'Login'
    metadata['Tester'] = 'API Team'


