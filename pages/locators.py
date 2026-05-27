from selenium.webdriver.common.by import By


class MainPageLocators():
    GOOGLE_HEADLINE = (By.CSS_SELECTOR, "[aria-label='Google']")
    SEARCH_BOX = (By.CSS_SELECTOR, "[class='gLFyf']")