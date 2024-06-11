import os
import pytest
import requests
import allure
from datetime import datetime
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.options.android import UiAutomator2Options
from dotenv import dotenv_values, load_dotenv

load_dotenv()
config = dotenv_values(".env")

app_package = 'com.saucelabs.mydemoapp.rn'
app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'midterm_project', 'app', 'MyDemoApp.apk')


def pytest_addoption(parser):
    parser.addoption("--mode_run", action="store", default="local_em", help="Choose to run mode: local_em, remote_bs")


@pytest.fixture(scope='function', autouse=True)
def app(request):
    appium_driver = None
    mode_run = request.config.getoption("--mode_run")
    if mode_run == "local_em":
        capabilities = {
            'platformName': 'android',
            'deviceName': '@Pixel_3a_API_34',
            'appium:automationName': 'UIAutomator2',
            'appium:app': app_path
        }
        options = AppiumOptions().load_capabilities(capabilities)
        appium_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    elif mode_run == "remote_bs":
        capabilities = {
            'platformName': 'android',
            'platformVersion': '9.0',
            'deviceName': 'Google Pixel 3a',
            'app': uploaded_app_url(),

            'bstack:options': {
                "projectName": "My Demo Project",
                "buildName": "browserstack-build-3",
                f"sessionName": f"{request.node.name}",

                # Set access credentials
                "userName": config['BROWSERSTACK_USERNAME'],
                "accessKey": config['BROWSERSTACK_ACCESS_KEY']
            }

        }
        options = UiAutomator2Options().load_capabilities(capabilities)
        appium_driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    print("\nStarting appium..")
    yield appium_driver
    print("\nQuitting appium...")
    appium_driver.quit()


# @pytest.fixture()
# def app(appium_driver):
#     print("Starting app...")
#     appium_driver.activate_app(app_package)
#     yield appium_driver
#     print("\nTerminating app...")
#     appium_driver.terminate_app(app_package)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs['app']
        take_screenshot(driver, item.nodeid)
        if item.config.getoption("--mode_run") == "remote_bs":
            take_video_record(driver, item.nodeid)


def take_screenshot(driver, nodeid: str) -> None:
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{nodeid}_{now}.png".replace("/", "_").replace("::", "__")
    allure.attach(driver.get_screenshot_as_png(), name=filename, attachment_type=allure.attachment_type.PNG)


def take_video_record(driver, nodeid: str) -> None:
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{nodeid}_{now}.mp4".replace("/", "_").replace("::", "__")
    body = f"""<html><body><video width='100%' height='100%' controls autoplay><source 
    src='{get_video_url(driver.session_id)}' 
    type='video/mp4'></video></body></html>"""
    allure.attach(body=body, name=filename, attachment_type=allure.attachment_type.HTML)


# Get video url by session id
def get_video_url(session_id):
    url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
    data = requests.get(url=url, auth=(config['BROWSERSTACK_USERNAME'], config['BROWSERSTACK_ACCESS_KEY'])).json()
    return data["automation_session"]["video_url"]


# Uploaded app and return app_url form browserstack
def uploaded_app_url():
    files = {'file': open(app_path, 'rb')}
    url = f"https://api-cloud.browserstack.com/app-automate/upload"
    response = requests.post(url=url, files=files, auth=(config['BROWSERSTACK_USERNAME'],
                                                         config['BROWSERSTACK_ACCESS_KEY']))
    return response.json().get("app_url")