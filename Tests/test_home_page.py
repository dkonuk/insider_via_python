from Pages.HomePage import HomePage
from Test_Data import test_Data
import time
# use python -m pytest to run test
# for only chrome use   python -m pytest -k Chrome

class Test_HomePage():


    def test_homepage(self, fixtureSetup):
        driver = fixtureSetup
        driver.get(test_Data.test_Data.url)

        # Accept cookies if present
        try:
            HomePage(driver).clic_accept_all()
        except:
            pass

        # Verify page loaded successfully
        assert HomePage(driver).check_if_page_loaded(), "Home page did not load successfully"

        # Click on the "Careers" link
        HomePage(driver).click_careers_in_Steps()
        time.sleep(2)
        # Check if careers block loaded

        HomePage(driver).check_careers_block()
        HomePage(driver).check_locations_block()
        HomePage(driver).check_life_At_insider_block()
        HomePage(driver).click_see_all_teams()
        time.sleep(1)
        HomePage(driver).click_quality_assurance()
        HomePage(driver).click_see_all_qa_jobs()
        time.sleep(2)
        HomePage(driver).set_location_filter2("Istanbul")
        time.sleep(1)
        assert HomePage(driver).are_there_jobs(), "There eno jobs available right now"
        assert HomePage(driver).is_department_correct(), "Department for this position is not correct"
        assert HomePage(driver).is_location_correct(), "Location for this position is not correct"
        HomePage(driver).close_location_filter()
        HomePage(driver).click_view_role_button()
        time.sleep(5)
        driver.quit()




