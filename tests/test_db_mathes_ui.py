from model.group import Group
from model.contact import Contact

def test_group_list(app,db):
    ui_group = app.group.get_groups_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    bd_group = map(clean,db.get_group_list())
    assert sorted(ui_group,key=Group.id_or_max) == sorted(bd_group, key=Group.id_or_max)

def test_contact_list(app,db):
    ui_contact = app.contact.get_contacts_list()
    def clean(contact):
        return Contact(id=contact.id,firstname = ''.join(contact.firstname.split(' ')),lastname = ''.join(contact.lastname.split(' ')))
    bd_contact = map(clean,db.get_contact_list())
    assert  sorted(ui_contact,key=Contact.id_or_max) == sorted(bd_contact, key=Contact.id_or_max)
