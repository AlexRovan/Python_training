# -*- coding: utf-8 -*-W
from model.contact import Contact
import random


def test_edit_contact_by_index(app,json_contact,db):
    contact = json_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    edit_contact = random.choice(old_contacts)
    contact.id = edit_contact.id
    app.contact.edit_contact_by_id(contact,edit_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(edit_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)