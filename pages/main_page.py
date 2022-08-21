from pages.base import Base
from selenium.webdriver.common.by import By


class MainPage(Base):

    CONFIRM_TOWN_BUTTON = (By.ID, 'ru.beru.android:id/skipButton')
    # SEARCH_INPUT = (By.ID, 'ru.beru.android:id/viewSearchAppBarLayoutInput')
    SEARCH_INPUT = (By.ID, 'ru.beru.android:id/viewSearchAppBarLayoutInputClickArea')
    SEARCH_ICON = (By.ID, 'ru.beru.android:id/viewSearchAppBarLayoutSearchIcon')