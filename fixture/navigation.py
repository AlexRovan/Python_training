

class Navigation:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(wd.find_elements_by_link_text("home")) > 0):
            wd.get("http://localhost/addressbook/")

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("*/addressbook/") and len(wd.find_elements_by_link_text("home")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("*/edit.php") and len(wd.find_elements_by_link_text("add new")) > 0):
            wd.find_element_by_link_text("add new").click()

    # group navigation
    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("*/group.php") and len(wd.find_elements_by_link_text("group page")) > 0):
            wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("*/group.php") and len(wd.find_elements_by_link_text("groups")) > 0):
            wd.find_element_by_link_text("groups").click()

