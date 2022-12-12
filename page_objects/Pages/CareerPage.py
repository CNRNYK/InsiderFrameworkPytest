from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CareerPage(BasePage):
    locations_section = (By.XPATH, "//section[@id='career-our-location']")
    teams_section = (By.XPATH, "//div[@data-id='b6c45b2']")
    life_at_insider_section = (By.XPATH, "//section[@data-id='a8e7b90']")
    see_all_teams_button = (By.XPATH, "//a[text()='See all teams']")
    quality_assurance_button = (By.XPATH, "//a//h3[text()='Quality Assurance']")

    def verify_page_element_displayed(self):
        self.verify_element_displayed(self.locations_section, name_of_element="Location Section")
        self.verify_element_displayed(self.teams_section, name_of_element="Team Section")
        self.verify_element_displayed(self.life_at_insider_section, name_of_element="Life at insider Section")
        return self

    def scroll_click_see_all_teams(self):
        self.scroll_to_element_by_locator(self.see_all_teams_button)
        self.wait_for_click(self.see_all_teams_button)
        self.click_element(self.see_all_teams_button)
        return self

    def scroll_click_qa(self):
        self.scroll_to_element_by_locator(self.quality_assurance_button, element_name="QA Button")
        self.wait_for_click(self.quality_assurance_button, name_of_element="QA Button")
        self.click_element(self.quality_assurance_button, name_of_element="QA Button")
        return self
