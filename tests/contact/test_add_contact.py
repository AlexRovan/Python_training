# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact

empty = Contact(firstname="",lastname= "",company="",address="",home="",mobile_phone="",work_phone="", email_1="")

def random_string(prefix,maxlen = 10):
    symbols = string.ascii_letters + string.punctuation + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [empty] +[Contact(firstname= random_string("firstname_",15),
                     lastname= random_string("lastname_",30),
                     company= random_string("company_",15),
                     address= random_string("address_",40),
                     home= random_string("home_",10),
                     mobile_phone= random_string("mobile_phone_",10),
                     work_phone= random_string("work_phone_",10),
                     second_phone =random_string("work_phone_",10),
                     email_1=random_string("email_1_",10),
                     email_2=random_string("email_2_",10),
                     email_3=random_string("email_3_",10))
                     for i in range(5)
                     ]

@pytest.mark.parametrize("contact",testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts=app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)




