import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.navigator.open_home_page()
        wd = self.app.wd
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        time.sleep(1)

    def is_login_open(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))

    def is_loggin_in_as(self,username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text == "("+username+")"

    def login_ensure(self, username, password):
        if self.is_login_open() > 0:
            if self.is_loggin_in_as(username):
                return

            self.logout()
            self.login(username, password)

        self.login(username, password)

    def logout_ensure(self):
        if self.is_login_open() > 0:
            self.logout()
