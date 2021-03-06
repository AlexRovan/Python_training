from model.group import Group


class GroupHelper:

    group_cache = None

    def __init__(self, app):
        self.app = app

    def add_new_group(self):
        wd = self.app.wd
        self.app.navigator.open_group_page()
        wd.find_element_by_name("new").click()

    def create(self, group):
        wd = self.app.wd
        self.add_new_group()
        self.fill_group(group)
        # submit group
        wd.find_element_by_name("submit").click()
        self.app.navigator.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[ value='%s']" % id).click()

    def delete_group_by_index(self,index):
        wd = self.app.wd
        self.app.navigator.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.app.navigator.return_to_group_page()
        self.group_cache = None

    def delete_group_by_id(self,id):
        wd = self.app.wd
        self.app.navigator.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.app.navigator.return_to_group_page()
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_group_by_index(group,0)

    def edit_group_by_index(self, group,index):
        wd = self.app.wd
        self.app.navigator.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        wd.find_element_by_name("update").click()
        self.app.navigator.return_to_group_page()
        self.group_cache = None

    def edit_group_by_id(self, group, id):
        wd = self.app.wd
        self.app.navigator.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        wd.find_element_by_name("update").click()
        self.app.navigator.return_to_group_page()
        self.group_cache = None

    def fill_group(self, group):
        self.set_field("group_name", group.name)
        self.set_field("group_header", group.header)
        self.set_field("group_footer", group.footer)

    def set_field(self, field_name, text):
        wd = self.app.wd

        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        self.app.navigator.open_group_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigator.open_group_page()
            group_cache = []
            for el in wd.find_elements_by_css_selector("span.group"):
                text = el.text
                id = el.find_element_by_name("selected[]").get_attribute("value")
                group_cache.append(Group(name=text,id = id))
        return list(group_cache)
 