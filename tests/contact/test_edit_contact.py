# -*- coding: utf-8 -*-W
from model.contact import Contact
import random


empty = Contact(firstname="",lastname= "",company="",address="",home="",mobile_phone="",work_phone="", email_1="")
contact_edit = Contact(firstname="Alex_edit",lastname= "Rovan_edit",company= "CFT_edit",address= "Novosibirsk_edit",home="123321321",mobile_phone= "12331223",work_phone= "413243243",email= "weqwwe_edit@sffse.ri")
contact_edit_phone = Contact(mobile_phone="88005553535")
contact_edit_email = Contact(email_1="new_email@mail.ru")


def test_edit_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(empty)
    old_contacts = app.contact.get_contacts_list()
    index = random.randrange(len(old_contacts))
    contact_edit.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact_edit,index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact_edit
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)


#def test_edit_phone_first_contact(app):
#    if app.contact.count()== 0:
#        app.contact.create(empty)
#    old_contacts = app.contact.get_contacts_list()
#    app.contact.edit_first_contact(contact_edit_phone)
#    new_contacts = app.contact.get_contacts_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_edit_email_first_contact(app):
#    if app.contact.count()== 0:
#        app.contact.create(empty)
#    old_contacts = app.contact.get_contacts_list()
#    app.contact.edit_first_contact(contact_edit_email)
#    new_contacts = app.contact.get_contacts_list()
#    assert len(old_contacts) == len(new_contacts)