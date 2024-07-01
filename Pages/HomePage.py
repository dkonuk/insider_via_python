from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class HomePage(BasePage):
    cookies_accept_button = (By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
    nav_bar_load = (By.CSS_SELECTOR, "#navbarNavDropdown")
    nav_bar_company = (By.CSS_SELECTOR, 'body > nav:nth-child(6) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(6) > a:nth-child(1)')
    nav_bar_company_carreers = (By.CSS_SELECTOR, 'body > nav:nth-child(6) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(6) > div:nth-child(2) > div:nth-child(2) > a:nth-child(2)')
    careers_block = (By.XPATH, '//*[@id="career-find-our-calling"]/div/div')
    locations_block = (By.XPATH, '//*[@id="career-our-location"]/div/div')
    life_at_insider_block = (By.XPATH, '/html/body/div[2]/div[3]')
    see_all_teams = (By.XPATH, '//*[@id="career-find-our-calling"]/div/div/a')
    QA_page_link = (By.CSS_SELECTOR, "#career-find-our-calling > div > div > div.col-12.d-flex.flex-wrap.p-0.career-load-more > div:nth-child(23) > div.job-title.mt-0.mt-lg-2.mt-xl-5 > a > h3")
    see_all_qa_jobs = (By.CSS_SELECTOR, ".btn-outline-secondary")
    location_filter = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
    location_filter_show_items = (By.XPATH, '//*[@id="select2-filter-by-location-results"]')
    location_istanbul = (By.CSS_SELECTOR, '#select2-filter-by-location-result-lk1c-Istanbul')
    LOCATION_SELECTION = (By.CSS_SELECTOR, "#filter-by-location > option.job-location.istanbul-turkey")
    job_list = (By.CSS_SELECTOR, "#jobs-list")
    job_list_department = (By.CSS_SELECTOR, ".position-department")
    job_list_location = (By.CSS_SELECTOR, ".position-location")
    team = "Quality Assurance"
    location = "Istanbul"

    def __init__(self, driver):
        super().__init__(driver)

    def clic_accept_all(self):
        BasePage.click_action(self, self.cookies_accept_button)

    def check_if_page_loaded(self):
        return BasePage.element_displayed_status(self, self.nav_bar_load)

    def click_careers_in_Steps(self):
        BasePage.click_action(self, self.nav_bar_company)
        time.sleep(1)
        BasePage.click_action(self, self.nav_bar_company_carreers)

    def check_careers_block(self):
        BasePage.element_displayed_status(self, self.careers_block)

    def check_locations_block(self):
        BasePage.element_displayed_status(self, self.locations_block)

    def check_life_At_insider_block(self):
        BasePage.element_displayed_status(self, self.life_at_insider_block)

    def click_see_all_teams(self):
        BasePage.click(self, self.see_all_teams)

    def click_quality_assurance(self):
        BasePage.scroll_to_element(self, self.QA_page_link)

    def click_see_all_qa_jobs(self):
        BasePage.click_action(self, self.see_all_qa_jobs)

    def set_location_filter2(self, location):
        print(f"Clicking on location filter: {self.location_filter}")
        self.click_by(self.location_filter)
        time.sleep(1)
        location_element = list(self.LOCATION_SELECTION)
        location_element[1] = self.LOCATION_SELECTION[1].format(location)
        self.LOCATION_SELECTION = tuple(location_element)

        print(f"Scrolling to location: {self.LOCATION_SELECTION}")
        self.scroll_to_element(self.LOCATION_SELECTION)
        time.sleep(1)
        print(f"Clicking on location selection: {self.LOCATION_SELECTION}")
        self.click_by(self.LOCATION_SELECTION)

    def are_there_jobs(self):
        positions = self.get_elements(self.job_list)
        if len(positions) > 0:
            return True
        else:
            return False

    def is_department_correct(self):
        positions_department = self.get_elements(self.job_list_department)
        for position in positions_department:
            is_position_correct = position.text == self.team
            if is_position_correct == False:
                return False

        return True

    def is_location_correct(self):
        positions_location = self.get_elements(self.job_list_location)
        for position in positions_location:
            print(position.text)
            is_position_correct = position.text.__contains__( self.location)
            if is_position_correct == False:
                return False

        return True




