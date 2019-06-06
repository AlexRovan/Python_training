from model.contact import Contact
import random
import data.group
import data.contact


def test_contact_add_group(app,db,check_ui):
    if len(db.get_contact_list())==0:
        app.contact.create(data.contact.testdata)
    if len(db.get_group_list())==0:
        app.group.create(data.group.testdata)
    all_contacts = db.get_contact_list()
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    contact = random.choice(all_contacts)
    old_contacts_in_groups=db.get_contact_in_group(group)
    app.contact.add_contact_to_group_list(contact,group)
    old_contacts_in_groups.append(contact)
    new_contacts_in_groups = db.get_contact_in_group(group)
    assert sorted(old_contacts_in_groups,key = Contact.id_or_max) == sorted(new_contacts_in_groups,key=Contact.id_or_max)
