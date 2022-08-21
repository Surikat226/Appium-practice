from pages.main_page import MainPage


def test_1_emulator(driver):
  main_page = MainPage(driver)

  main_page.click_on_element(main_page.CONFIRM_TOWN_BUTTON)
  main_page.enter_text(main_page.SEARCH_INPUT, 'Волшебная ракушка')
  main_page.click_on_element(main_page.SEARCH_ICON)