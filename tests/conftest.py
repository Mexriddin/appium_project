import os.path
import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions

app_package = 'com.saucelabs.mydemoapp.rn'


@pytest.fixture(scope='session', autouse=True)
def appium_driver():
    capabilities = {
        'platformName': 'android',
        'deviceName': '@Pixel_3a_API_34',
        'appium:automationName': 'UIAutomator2',
        'appium:app': 'C:\\Users\\mexriddin maxkamtaev\\PycharmProjects\\appium-homework-pr\\midterm_project\\app\MyDemoApp.apk'
        # 'appium:app': f'{os.path.dirname(os.getcwd())}\\midterm_project\\app\MyDemoApp.apk'

    }
    options = AppiumOptions().load_capabilities(capabilities)
    appium_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    print("\nStarting appium..")
    yield appium_driver
    # print("Removing app...")
    # appium_driver.remove_app(app_package)
    print("Quitting appium...")
    appium_driver.quit()


@pytest.fixture()
def app(appium_driver):
    print("Starting app...")
    appium_driver.activate_app(app_package)
    yield appium_driver
    print("\nTerminating app...")
    appium_driver.terminate_app(app_package)
