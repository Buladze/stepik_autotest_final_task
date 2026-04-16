import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "https://www.google.com/?hl=en"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[aria-label='Google']")