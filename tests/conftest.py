import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
import os
from dotenv import load_dotenv

load_dotenv()

CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "driver" in item.fixturenames:
                web_driver = item.funcargs["driver"]
                allure.attach(web_driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
