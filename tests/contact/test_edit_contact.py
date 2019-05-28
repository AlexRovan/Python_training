# -*- coding: utf-8 -*-W
from model.contact import Contact
import random


def test_edit_contact_by_index(app,json_contact):
    contact = json_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contacts_list()
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact,index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)