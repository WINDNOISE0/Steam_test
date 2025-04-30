from elements.button import Button
from elements.label import Label
from elements.multy_web_element import MultyWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Hovers')]"
    USER_CARS_LOC = "//div[@class='figure']"

    USER_CARD_LOC_TEMP = "(//img[@alt='User Avatar'])[{}]"

    VIEW_PROFILE_BUTTON_LOC_TEMP = "//a[@href='/users/{}']"
    USER_CARD_DATA_LOC_TEMP = "//div[@class='figcaption']/*[contains(text(), 'name: user{}')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.users_cards = MultyWebElement(browser, self.USER_CARS_LOC)

        self.user_card = None
        self.view_profile_button = None
        self.user_card_data = None

    def hover_random_user(self, user_number):
        self.user_card = WebElement(self.browser, self.USER_CARD_LOC_TEMP.format(user_number))
        self.view_profile_button = Button(self.browser, self.VIEW_PROFILE_BUTTON_LOC_TEMP.format(user_number))
        self.user_card_data = Label(self.browser, self.USER_CARD_DATA_LOC_TEMP.format(user_number))

        self.user_card.move_to_element()

    def click_view_profile(self):
        self.view_profile_button.click()

    @property
    def actual_user_number(self):
        return int(self.user_card_data.get_text()[-1])

    @property
    def actual_user_link(self):
        return self.browser.get_current_link()

    @property
    def user_count(self):
        return self.users_cards.get_count_item_teg()
