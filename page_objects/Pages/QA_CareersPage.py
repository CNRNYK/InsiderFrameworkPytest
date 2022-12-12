from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class QACareerPage(BasePage):
    see_all_qa_jobs_button = (By.XPATH, "//*[contains(text(), 'See all QA jobs')]")
    locations_section = (By.XPATH, "//section[@id='career-our-location']")

    def click_to_see_jobs(self):
        self.scroll_to_element_by_locator(self.see_all_qa_jobs_button, element_name="See all qa jobs")
        self.wait_for_click(self.see_all_qa_jobs_button)
        self.click_element(self.see_all_qa_jobs_button, name_of_element="See all qa button")
        return self
