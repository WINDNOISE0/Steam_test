from elements.button import Button
from elements.label import Label
from elements.multy_web_element import MultyWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Hovers')]"
    USER_CARS_LOC = "(//div[contains(@class, 'figure')])[{}]"

    USER_CARD_LOC_TEMP = "(//img[@alt='User Avatar'])[{}]"

    VIEW_PROFILE_BUTTON_LOC_TEMP = "//a[@href='/users/{}']"
    USER_CARD_DATA_LOC_TEMP = "//div[contains(@class, 'figcaption')]/*[contains(text(), 'name: user{}')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.users_cards = MultyWebElement(browser, self.USER_CARS_LOC)

    def hover_random_user(self, user_number):
        user_card = WebElement(self.browser, self.USER_CARD_LOC_TEMP.format(user_number))
        user_card.move_to_element()

    def click_view_profile(self, user_number):
        view_profile_button = Button(self.browser, self.VIEW_PROFILE_BUTTON_LOC_TEMP.format(user_number))
        view_profile_button.click()

    def get_actual_user_number(self, user_number):
        user_card_data = Label(self.browser, self.USER_CARD_DATA_LOC_TEMP.format(user_number))
        return int(user_card_data.get_text()[-1])

    @property
    def actual_user_link(self):
        return self.browser.get_current_link()

    @property
    def user_count(self):
        return self.users_cards.get_count_item_tag()
