from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(element))

    def click(self, element):
        x = self.find_element(element)
        x.send_keys(Keys.ENTER)

    def click_action(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).click()

    def enter_text(self, element, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).send_keys(text)

    def get_text(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).text()

    def element_displayed_status(self, element):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).is_displayed()

    def dropdown_menu_select(self, element1, element2):
        action = ActionChains(self.driver)
        page = self.driver.find_element(element1)
        action.click(page).perform()
        second_menu = self.driver.find_element(element2)
        action.click(second_menu)

    def dropdown_menu_select_first_element(self, element):
        action = ActionChains(self.driver)
        page = self.driver.find_element(element)
        action.move_to_element(page).perform()
        action.click(page).perform()

    def scroll_to_element(self, element):
        clickings = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click()", clickings)

    def click_by(self, element):
        elem = self.find_element(element)
        elem.click()

    def get_elements(self, element):
        return self.driver.find_elements(*element)

    def escape(self):
       ActionChains(self.driver)\
        .send_keys(Keys.ESCAPE)\
        .perform()
