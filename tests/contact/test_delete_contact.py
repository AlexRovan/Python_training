# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import time
from data.contact import empty


def test_delete_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(empty)
    old_contacts = app.contact.get_contacts_list()
    index = random.randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts
