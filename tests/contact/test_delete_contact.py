# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import time
from data.contact import empty


def test_delete_contact_by_index(app,db,check_ui):
    if app.contact.count() == 0:
        app.contact.create(empty)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(1)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert new_contacts == old_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),key=Contact.id_or_max)