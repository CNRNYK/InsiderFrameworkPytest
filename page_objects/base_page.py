import sys
import time
import logging
from selenium.webdriver.common.by import By

from config.base_config import BaseConfig
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSelectorException, JavascriptException
from assertpy import assert_that, fail

"""This class is the parent of all classes"""
"""It contains all the generic methods and utilities for all pages"""
logger = logging.getLogger(__name__)


class BasePage:
    COOKIE_BANNER_ACCEPT_BUTTON = (By.XPATH, "//a[@id='wt-cli-accept-all-btn']")

    def __init__(self, driver):
        self.driver = driver
        self.timeout = BaseConfig.DEFAULT_WAIT
        self.long_timeout = BaseConfig.LONG_WAIT

    def visit(self, url):
        self.driver.get(url)
        logger.info(f'Opened page {url}.')
        return self

    def print_current_url(self):
        logger.warning(f'CURRENT URL = {self.get_current_url()}')
        return self

    def find_element(self, locator, visibility=True):
        if visibility:
            return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator),
                                                                  f'ELEMENT IS NOT FOUND OR VISIBLE! => {locator}')
        else:
            return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator),
                                                                  f'ELEMENT IS NOT FOUND! => {locator}')

    def click_element(self, locator, name_of_element=None):
        self.wait_for_element(locator)
        self.verify_element_is_clickable(locator, name_of_element).click()
        logger.info(f'Click on: "{name_of_element}".')
        return self

    def click_execute_script(self, locator):
        self.scroll_to_element_by_locator(locator)
        self.driver.execute_script("window.scrollBy(0,250);")
        self.driver.execute_script("arguments[0].click();", locator)
        return self

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element(self, locator, element_name=None, timeout=BaseConfig.LONG_WAIT):
        element = WebDriverWait(self.driver, timeout) \
            .until(ec.presence_of_element_located(locator), f'{locator} not present - could not be located')
        WebDriverWait(self.driver, timeout) \
            .until(ec.element_to_be_clickable(locator), f'{locator} not clickable - could not be clicked')
        logger.info(f'Wait for element "{element_name}" to be present and clickable.')
        return element

    def wait_for_click(self, locator, name_of_element=None):
        time.sleep(5)
        return self

    def verify_element_is_clickable(self, locator, name_of_element=None):
        try:
            logger.info(f'Verification if element is clickable: "{name_of_element}".')
            return WebDriverWait(self.driver, self.long_timeout).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            logger.error(f'\nTimeoutException! Element "{name_of_element}" was not found by locator: {locator}.')
        except InvalidSelectorException:
            logger.error(
                f'\nInvalidSelectorException! Element "{name_of_element}" was not found by locator: {locator}.')
        except:
            logger.error(f'Error! The {sys.exc_info()[0]} has occurred!!!!')
        return self

    def verify_text(self, expected_text, timeout=BaseConfig.LONG_WAIT):
        try:
            i = 1
            while i <= timeout:
                if expected_text in self.driver.page_source:
                    logger.info(f'Verification: Text "{expected_text}" is present.')
                    break
                else:
                    time.sleep(1)
                    i += 1
            page_source = self.driver.page_source
            assert_that(page_source).contains(expected_text)
        except AttributeError:
            raise AttributeError(f'Expected text "{expected_text}" is not found on the page!')
        except AssertionError:
            raise AssertionError(f'Expected text "{expected_text}" is not found on the page!')
        except:
            logger.error(f'Error! The {sys.exc_info()[0]} has occurred!!!!')
        return self

    def verify_element_displayed(self, locator, name_of_element=None):
        WebDriverWait(self.driver, self.long_timeout).until(ec.visibility_of_element_located(locator),
                                                            f'Element "{name_of_element}" expected to be visible is not '
                                                            f'displayed! =>  {locator}')
        logger.info(f'Verification: Element "{name_of_element}" is present.')
        return self

    def verify_element_not_displayed(self, locator, name_of_element=None, timeout=BaseConfig.DEFAULT_WAIT):
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator),
                                                  f'Element expected not to be visible is displayed! Locator => {locator}')
        logger.info(f'Verification: Element "{name_of_element}" is NOT present.')
        return self

    def verify_element_text(self, locator, expected_text):
        WebDriverWait(self.driver, self.timeout).until(ec.text_to_be_present_in_element(locator, expected_text),
                                                       f'Timeout! Element by locator = {locator},has not text = '
                                                       f'{expected_text}')
        return self

    def verify_title_to_be(self, expected_title, timeout=BaseConfig.DEFAULT_WAIT):  # TODO check where it is used
        actual_title = self.driver.title
        try:
            i = 1
            while i <= timeout:
                if assert_that(actual_title).is_equal_to(expected_title):
                    logger.info(f'Verification:\nCurrent Title = "{actual_title}", '
                                f'is equal to \nExpected Title = "{expected_title}".')
                    break
                else:
                    time.sleep(1)
                    i += 1
        except TimeoutException:
            raise TimeoutException(f'\nTimeoutException! Timeout waiting for title => "{expected_title}".')
        except AttributeError:
            raise AttributeError(f'AttributeError ========> {sys.exc_info()}')
        except AssertionError:
            raise AssertionError(f'\nActual Title = "{actual_title}", '
                                 f'does not equal to \nExpected Title = "{expected_title}".')
        except:
            logger.error(f'Error! The {sys.exc_info()[0]} has occurred!!!!')
        return self

    def wait_for_title_to_be(self, expected_title):  # TODO check where it is used and if it is relevant
        WebDriverWait(self.driver, self.timeout).until(ec.title_is(expected_title),
                                                       f'TIMEOUT!! Timeout waiting for title => {expected_title}')
        logger.info(f'Verification: Page Title = "{expected_title}".')
        return self

    def scroll_to_element_by_locator(self, element_locator, element_name=None):
        logger.info(f'Scroll to element: {element_name}')
        try:
            self.driver.execute_script("""arguments[0].scrollIntoView({
            behavior: 'auto',
            block: 'center',
            inline: 'center',
        });""", self.find_element(element_locator))
        except JavascriptException as e:
            error = e.args[0]
            raise JavascriptException(error) from e.__cause__
        return self

    def click_cookie_banner_accept_button(self):
        self.click_element(self.COOKIE_BANNER_ACCEPT_BUTTON, 'Cookie banner accept button')
        logger.info(f'Cookie banner dismissed')
        return self

    def hover_on_element(self, locator, locator2, element_name=None):
        ActionChains(self.driver).move_to_element(self.find_element(locator)).perform()
        logger.info(f'Hover over the: "{element_name}".')
        return self

    def hover_on_element_and_click(self, locator, locator2, element_name=None):
        self.hover_on_element(locator, element_name)
        self.click_element(locator2, element_name)
        self.wait_for_click(locator2)
        return self

    def switch_to_new_tab(self, job_lever):
        second_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(second_tab)
        logger.info('Switch to new tab.')
        time.sleep(2)  # Without time.sleep here test failed locally.
        current_url = self.get_current_url()
        assert_that(current_url).contains(job_lever)
        logger.info(f'Current URL "{current_url}". contains "{job_lever}"')
        return self
