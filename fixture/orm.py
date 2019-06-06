from pony.orm import *
from model.group import Group
from model.contact import Contact
from datetime import datetime


class ORM_fixture:

    db = Database()

    def __init__(self,host,database,user,password):
        self.db.bind("mysql",host=host,database=database,user=user,password=password)
        self.db.generate_mapping()
        sql_debug(True)

    class ORM_Group(db.Entity):
        _table_='group_list'
        id = PrimaryKey(int, column ='group_id')
        name = Optional(str,column ='group_name')
        header = Optional(str,column ='group_header')
        footer = Optional(str,column ='group_footer')
        contacts = Set(lambda : ORM_fixture.ORM_Contact, table='address_in_groups',column='id', reverse='groups',lazy=True)

    class ORM_Contact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        second_phone = Optional(str, column='phone2')
        deprecated = Optional(datetime, column= 'deprecated')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        groups = Set(lambda: ORM_fixture.ORM_Group, table='address_in_groups',column='group_id',reverse='contacts',lazy=True)

    def convert_group(self,groups):
        def convert(group):
            return Group(id=str(group.id),header=group.header,name=group.name,footer=group.footer)
        return list(map(convert,groups))

    def convert_contact(self,contacts):
        def convert(contact):
            return Contact(id=str(contact.id),
                           firstname =contact.firstname,
                           lastname = contact.lastname,
                           address=contact.address,
                           home= contact.home,
                           work_phone= contact.work_phone,
                           mobile_phone=contact.mobile_phone,
                           second_phone=contact.second_phone,
                           email_1=contact.email,
                           email_2=contact.email2,
                           email_3=contact.email3)

        return list(map(convert,contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contact(select(c for c in ORM_fixture.ORM_Contact if c.deprecated is None))

    @db_session
    def get_group_list(self):
        return self.convert_group(select(g for g in ORM_fixture.ORM_Group))

    @db_session
    def get_contact_in_group(self, group):
        orm_group = list(select(g for g in ORM_fixture.ORM_Group if g.id == group.id))[0]
        return self.convert_contact(orm_group.contacts)

    @db_session
    def get_contact_in_not_group(self, group):
        orm_group = list(select(g for g in ORM_fixture.ORM_Group if g.id == group.id))[0]
        return self.convert_contact(select(c for c in ORM_fixture.ORM_Contact if c.deprecated is None and orm_group not in c.groups ))