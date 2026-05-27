from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage): 
    def go_to_search(self):
        login_link = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        login_link.click()
    
    def should_be_headline(self):
        assert self.is_element_present(*MainPageLocators.GOOGLE_HEADLINE), "Should be 'Google'"