# -*- coding: utf-8 -*-

from model.contact import Contact

father = Contact("Alex", "Rovan", "CFT", "Novosibirsk", "123321321", "12331223", "413243243", "weqwwe@sffse.ri")
empty = Contact("", "", "", "", "", "", "", "")


def test_add_contact(app):
    old_contacts=app.contact.get_contacts_list()
    app.contact.create(father)
    new_contacts=app.contact.get_contacts_list()
    assert len(old_contacts)+1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(empty)
    new_contacts=app.contact.get_contacts_list()
    assert len(old_contacts)+1 == len(new_contacts)






