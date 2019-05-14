
from model.contact import Contact


class ContactHelper:

    contact_cache = None

    def __init__(self,app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.navigator.add_new_contact()
        self.fill_field_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.navigator.return_home_page()
        self.contact_cache = None

    def edit_first_contact(self,contact):
        self.app.navigator.return_home_page()
        self.select_first_contact()
        self.click_edit()
        self.fill_field_contact(contact)
        self.click_update()
        self.app.navigator.return_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.app.navigator.return_home_page()
        self.select_first_contact()
        self.click_edit()
        self.click_delete()
        self.app.navigator.return_home_page()
        self.contact_cache = None

    def set_field(self, field_name, text):
        wd = self.app.wd

        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_field_contact(self, contact):
        self.set_field("firstname", contact.firstname)
        self.set_field("lastname", contact.lastname)
        self.set_field("company", contact.company)
        self.set_field("address", contact.address)
        self.set_field("home", contact.home)
        self.set_field("mobile", contact.mobile_phone)
        self.set_field("work", contact.work_phone)
        self.set_field("email", contact.email)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def click_edit(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()

    def click_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def click_delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()

    def count(self):
        wd = self.app.wd
        self.app.navigator.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigator.return_home_page
            contact_cache = []
            for row in  wd.find_elements_by_xpath("//tr[@name=\"entry\"]"):
                id = row.find_element_by_name("selected[]").get_attribute("id")
                cells = row.find_elements_by_css_selector("td")
                firstname = cells[2].text
                lastname = cells[1].text
                contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return contact_cache

