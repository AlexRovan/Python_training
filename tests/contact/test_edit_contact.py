# -*- coding: utf-8 -*-

from model.contact import Contact

contact_edit = Contact("Alex_edit", "Rovan_edit", "CFT_edit", "Novosibirsk_edit", "123321321", "12331223", "413243243", "weqwwe_edit@sffse.ri")


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(contact_edit)
    app.session.logout()