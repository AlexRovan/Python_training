# -*- coding: utf-8 -*-
from model.contact import Contact

empty = Contact("", "", "", "", "", "", "", "")


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(empty)
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert new_contacts == old_contacts