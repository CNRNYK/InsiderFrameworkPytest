import os
import time
import pytest

from utilities.logging.logging_base import LOGGER
from config.base_config import BaseConfig

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


def add_default_browser_argument(options):
    if BaseConfig.BROWSER == 'chrome':
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-cache')


    elif BaseConfig.BROWSER == 'firefox':
        options.add_argument('--private')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-cache')

    options.add_argument('--disable-popup-blocking')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-notifications')


@pytest.fixture(params=[BaseConfig.BROWSER], scope='function')
def init_driver(request):
    """
        params=["chrome"] can be params=["chrome", "firefox"] to make a case run on multiple browser
    """
    if BaseConfig.BROWSER == 'chrome':
        chrome_options = ChromeOptions()
        add_default_browser_argument(chrome_options)
        web_driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))

    elif BaseConfig.BROWSER == 'firefox':
        firefox_options = FirefoxOptions()
        add_default_browser_argument(firefox_options)
        web_driver = webdriver.Firefox(options=firefox_options, service=FirefoxService(GeckoDriverManager().install()))

    else:
        chrome_options = ChromeOptions()
        add_default_browser_argument(chrome_options)
        web_driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))

    request.cls.driver = web_driver
    LOGGER.info(f'Test {request.node.name} has started!')
    yield web_driver
    web_driver.quit()


@pytest.fixture
def teardown_fixture():
    """
        The yield block makes to run the code blocks once the test execution is finished.
        If yield block is deleted here, the code blocks run before the test execution starts.
    """
    yield
    print("If this fixture is added to any test, this comment line will be printed at the end of the test's execution")
    time.sleep(10)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):

            file_name = report.nodeid.replace("::", "_") + ".png"

            driver = item.funcargs['init_driver']
            driver.get_screenshot_as_file(file_name)

            if file_name:
                html = f'<div><img src="file:{os.path.dirname(os.path.abspath(__file__))}/%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
