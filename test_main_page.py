from .pages.main_page import MainPage
import pytest


def test_guest_can_go_to_start_page(browser, request):
    user_language = request.config.getoption("language")
    link = f"https://www.google.com/?hl={user_language}"
    page = MainPage(browser, link)
    page.open()
    page.go_to_search()
    page.should_be_headline()