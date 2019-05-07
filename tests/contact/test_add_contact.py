# -*- coding: utf-8 -*-

from model.contact import Contact

father = Contact("Alex", "Rovan", "CFT", "Novosibirsk", "123321321", "12331223", "413243243", "weqwwe@sffse.ri")
empty = Contact("", "", "", "", "", "", "", "")


def test_add_contact(app):
    app.contact.create(father)


def test_add_empty_contact(app):
    app.contact.create(empty)







