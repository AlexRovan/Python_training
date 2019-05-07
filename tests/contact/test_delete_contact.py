# -*- coding: utf-8 -*-
from model.contact import Contact

empty = Contact("", "", "", "", "", "", "", "")


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(empty)
    app.contact.delete_first_contact()
