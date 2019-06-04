import re
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

    def edit_contact_by_index(self,contact,index):
        self.app.navigator.return_home_page()
        self.click_edit_by_index(index)
        self.fill_field_contact(contact)
        self.click_update()
        self.app.navigator.return_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        self.app.navigator.return_home_page()
        self.click_edit_by_id(id)
        self.fill_field_contact(contact)
        self.click_update()
        self.app.navigator.return_home_page()
        self.contact_cache = None

    def delete_contact_by_index(self,index):
        self.app.navigator.return_home_page()
        self.select_contact_by_index(index)
        self.click_delete()
        self.app.navigator.return_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        self.app.navigator.return_home_page()
        self.select_contact_by_id(id)
        self.click_delete()
        self.app.navigator.return_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)
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
        self.set_field("email", contact.email_1)
        self.set_field("email2", contact.email_2)
        self.set_field("email3", contact.email_3)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def click_edit_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def click_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def click_view_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()

    def click_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def click_delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        self.app.navigator.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigator.return_home_page()
            contact_cache = []
            for row in wd.find_elements_by_xpath('//tr[@name="entry"]'):
                id = row.find_element_by_name("selected[]").get_attribute("id")
                cells = row.find_elements_by_css_selector("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phone = cells[5].text
                all_email = cells[4].text
                contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,address = address, all_phone_contact=all_phone, all_email_contact =all_email))
        return list(contact_cache)

    def get_contact_list_on_edit_page(self,index):
        wd = self.app.wd
        self.app.navigator.return_home_page()
        self.click_edit_by_index(index)
        id = wd.find_element_by_name("id")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text

        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        second_phone = wd.find_element_by_name("phone2").get_attribute("value")

        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(id=id, firstname=firstname, lastname=lastname,address= address, home=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, second_phone=second_phone, email_1=email_1, email_2=email_2, email_3=email_3)

    def get_contact_list_on_view_page(self, index):
        wd = self.app.wd
        self.app.navigator.return_home_page()
        self.click_view_by_index(index)
        all_view_text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)",all_view_text).group(1)
        work_phone = re.search("W: (.*)",all_view_text).group(1)
        mobile_phone = re.search("M: (.*)",all_view_text).group(1)
        second_phone = re.search("P: (.*)",all_view_text).group(1)
        return Contact(home=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, second_phone=second_phone)