# -*- coding: utf-8 -*-W
from model.contact import Contact

empty = Contact("", "", "", "", "", "", "", "")
contact_edit = Contact("Alex_edit", "Rovan_edit", "CFT_edit", "Novosibirsk_edit", "123321321", "12331223", "413243243", "weqwwe_edit@sffse.ri")
contact_edit_phone = Contact(mobile_phone="88005553535")
contact_edit_email = Contact(email="new_email@mail.ru")


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(empty)
    app.contact.edit_first_contact(contact_edit)


def test_edit_phone_first_contact(app):
    if app.contact.count()== 0:
        app.contact.create(empty)
    app.contact.edit_first_contact(contact_edit_phone)


def test_edit_email_first_contact(app):
    if app.contact.count()== 0:
        app.contact.create(empty)
    app.contact.edit_first_contact(contact_edit_email)