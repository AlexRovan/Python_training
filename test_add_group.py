# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def test_add_group(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/group.php")
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()
        dw.find_element_by_name("new").click()
        dw.find_element_by_name("group_name").click()
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_name").send_keys("gropup_1")
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_header").send_keys("dasdas")
        dw.find_element_by_name("group_footer").clear()
        dw.find_element_by_name("group_footer").send_keys("sasda")
        dw.find_element_by_name("submit").click()
        dw.find_element_by_link_text("group page").click()
        dw.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.dw.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.dw.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
