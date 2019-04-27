

class Navigation:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()