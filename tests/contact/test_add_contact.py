# -*- coding: utf-8 -*-

from model.contact import Contact

father = Contact(firstname= "Alex",lastname= "Rovan",company= "CFT",address= "Novosibirsk",home= "123321321",mobile_phone= "12331223",work_phone= "413243243",email="weqwwe@sffse.ri")
empty = Contact(firstname="",lastname= "",company="",address="",home="",mobile_phone="",work_phone="", email="")


def test_add_contact(app):
    old_contacts=app.contact.get_contacts_list()
    app.contact.create(father)
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(father)
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(empty)
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(empty)
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)





