import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.options.android import UiAutomator2Options
from dotenv import dotenv_values


config = dotenv_values(".env")
app_package = 'com.saucelabs.mydemoapp.rn'


def pytest_addoption(parser):
    parser.addoption("--mode_run", action="store", default="local_em", help="Choose to run mode: local_em, remote_bs")




@pytest.fixture(scope='session', autouse=True)
def appium_driver(request):
    appium_driver = None
    mode_run = request.config.getoption("--mode_run")
    if mode_run == "local_em":
        capabilities = {
            'platformName': 'android',
            'deviceName': '@Pixel_3a_API_34',
            'appium:automationName': 'UIAutomator2',
            'appium:app': 'C:\\Users\\mexriddin maxkamtaev\\PycharmProjects\\appium-homework-pr\\midterm_project\\app'
                          '\\MyDemoApp.apk'
        }
        options = AppiumOptions().load_capabilities(capabilities)
        appium_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


    elif mode_run == "remote_bs":
        capabilities = {
            'platformName': 'android',
            'platformVersion': '9.0',
            'deviceName': 'Google Pixel 3a',
            "app": "bs://7a04d670d0ee20c9499b17c676354d0f3243151d",

            'bstack:options': {
                "projectName": "My Demo Project",
                "buildName": "browserstack-build-2",
                "sessionName": "BStack first_test",

                # Set your access credentials
                "userName": config['BROWSERSTACK_USERNAME'],
                "accessKey": config['BROWSERSTACK_ACCESS_KEY']
            }

        }
        options = UiAutomator2Options().load_capabilities(capabilities)
        appium_driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    print("\nStarting appium..")
    yield appium_driver
    print("Quitting appium...")
    appium_driver.quit()


@pytest.fixture()
def app(appium_driver):
    print("Starting app...")
    appium_driver.activate_app(app_package)
    yield appium_driver
    print("\nTerminating app...")
    appium_driver.terminate_app(app_package)
