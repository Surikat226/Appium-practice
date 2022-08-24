import time

from pages.main_page import MainPage


def test_1_search_for_item(driver):
  main_page = MainPage(driver)

  main_page.single_tap_on_element(main_page.CONFIRM_TOWN_BUTTON)
  main_page.single_tap_on_element(main_page.SEARCH_INPUT)
  main_page.enter_text(main_page.SEARCH_INPUT_TEXT_ENTERING, 'Спанч боб')
  main_page.single_tap_on_element(main_page.SEARCH_ICON)