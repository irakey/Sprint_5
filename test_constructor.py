from locators import TestLocators
from data import URL


class TestConstructor:

    def test_constructor_buns_section_transition(self, driver):
        driver.get(URL)
        driver.execute_script("arguments[0].click();", driver.find_element(*TestLocators.TAB_BUNS))
        assert 'type_current' in driver.find_element(*TestLocators.ACTIVE_TAB_BUNS).get_attribute('class')
        driver.quit()

    def test_constructor_fillings_section_transition(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        assert 'type_current' in driver.find_element(*TestLocators.ACTIVE_TAB_FILLINGS).get_attribute('class')
        driver.quit()

    def test_constructor_sauces_section_transition(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        assert 'type_current' in driver.find_element(*TestLocators.ACTIVE_TAB_SAUCES).get_attribute('class')
        driver.quit()
