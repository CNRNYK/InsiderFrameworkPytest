import pytest

from config.base_config import BaseConfig
from page_objects.base_page import BasePage
from page_objects.Pages.CareerPage import CareerPage
from page_objects.Pages.HomePage import HomePage
from page_objects.Pages.OpenPositions_CareersPage import OpenPositions
from page_objects.Pages.QA_CareersPage import QACareerPage


@pytest.mark.usefixtures('init_driver')
@pytest.mark.e2e
class TestHomePage:

    def test_insider(self):
        base_page = BasePage(self.driver)
        base_page.visit(BaseConfig.APP_BASE_URL)
        base_page.click_cookie_banner_accept_button()
        homepage = HomePage(self.driver)
        homepage.verify_page_opened()
        homepage.click_more_button()
        homepage.click_career_button()

        career = CareerPage(self.driver)
        career.verify_page_element_displayed()

        career.scroll_click_see_all_teams()
        career.scroll_click_qa()

        qaOpenPage = QACareerPage(self.driver)
        qaOpenPage.click_to_see_jobs()


        openPage = OpenPositions(self.driver)
        openPage.click_required_job_opportunities()
        openPage.verify_job_lever_page_opened()







