from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.navigation import Navigation
from fixture.contact import Contact


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

        self.navigator = Navigation(self)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = Contact(self)

    def destroy(self):
        self.wd.quit()




