from time import sleep

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class OpenPositions(BasePage):
    location = "istanbul-turkey"
    department = "Quality Assurance"
    quality_assurance_jobs = (By.XPATH, "//div[@data-team='qualityassurance'][3]")  # todo bunu dinamik
    apply_jobs = (By.LINK_TEXT, "Apply Now")
    job_lever = "https://jobs.lever.co/useinsider/"

    def click_required_job_opportunities(self):
        self.hover_on_element_and_click(self.quality_assurance_jobs, self.apply_jobs)
        return self

    def verify_job_lever_page_opened(self):
        self.switch_to_new_tab(job_lever=self.job_lever)
