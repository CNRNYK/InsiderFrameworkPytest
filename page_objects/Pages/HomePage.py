from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HomePage(BasePage):

    more_button = (By.XPATH, "//a[normalize-space()='More']")
    more_selection_menu_career_button = (By.CSS_SELECTOR, "a[href='https://useinsider.com/careers/']")

    def verify_page_opened(self):
        self.verify_element_displayed(self.more_button, name_of_element="More Button")
        return self

    def click_more_button(self):
        self.click_element(self.more_button, name_of_element="More Button")
        return self

    def click_career_button(self):
        self.click_element(self.more_selection_menu_career_button, name_of_element="Career Button")
        return self




