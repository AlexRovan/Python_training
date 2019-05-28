# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app,json_contact):
    contact = json_contact
    old_contacts=app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)




