from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class HomePage(BasePage):
    cookies_accept_button = (By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
    nav_bar_load = (By.CSS_SELECTOR, "#navbarNavDropdown")
    nav_bar_company = (By.CSS_SELECTOR, 'li.nav-item:nth-child(6) > a:nth-child(1)')
    nav_bar_company_carreers = (By.CSS_SELECTOR, '.new-menu-dropdown-layout-6-mid-container > a:nth-child(2)')
    careers_block = (By.XPATH, '//*[@id="career-find-our-calling"]/div/div')
    locations_block = (By.XPATH, '//*[@id="career-our-location"]/div/div')
    life_at_insider_block = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div')
    see_all_teams = (By.XPATH, '//*[@id="career-find-our-calling"]/div/div/a')
    QA_page_link = (By.CSS_SELECTOR, "#career-find-our-calling > div > div > div.col-12.d-flex.flex-wrap.p-0.career-load-more > div:nth-child(23) > div.job-title.mt-0.mt-lg-2.mt-xl-5 > a > h3")
    see_all_qa_jobs = (By.CSS_SELECTOR, ".btn-outline-secondary")
    location_filter = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
    location_filter_show_items = (By.XPATH, '//*[@id="select2-filter-by-location-results"]')
    location_istanbul = (By.CSS_SELECTOR, '#select2-filter-by-location-result-lk1c-Istanbul\,\ Turkey')
    istanbul_id = "select2-filter-by-location-result-zrc3-Istanbul, Turkey"

    def __init__(self, driver):
        super().__init__(driver)

    def clic_accept_all(self):
        BasePage.click_action(self, self.cookies_accept_button)

    def check_if_page_loaded(self):
        return BasePage.element_displayed_status(self, self.nav_bar_load)

    def click_careers(self):
        BasePage.dropdown_menu_select(self, self.nav_bar_company, self.nav_bar_company_carreers)

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

    def select_location_filter(self):
        BasePage.click_action(self, self.location_filter)

    def select_istanbul(self):
        BasePage.click_action(self, self.location_istanbul)

    def selection(self):
        BasePage.click(self, self.location_istanbul)

    def selection_deneme(self):
        BasePage.dropdown_menu_select_first_element(self, self.location_istanbul)

    def click_istanbul(self):
        BasePage.scroll_to_element(self, self.location_istanbul)
        BasePage.click_by(self, self.location_istanbul)






