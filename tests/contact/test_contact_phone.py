import re
import random
from model.contact import Contact


bad_symbols = "() -"


def test_compare_contact_edit_and_home(app,db):

    active_contacts_bd = sorted(db.get_contact_list(), key=Contact.id_or_max)
    all_contact_on_home_page =  sorted( app.contact.get_contacts_list(), key=Contact.id_or_max)

    for i in range(len(all_contact_on_home_page)):
        contact_on_home_page = all_contact_on_home_page[i]
        contact_on_db = active_contacts_bd[i]

        assert contact_on_home_page.firstname == contact_on_db.firstname
        assert contact_on_home_page.lastname == contact_on_db.lastname
        assert contact_on_home_page.address == contact_on_db.address
        assert contact_on_home_page.all_phone_contact == merge_phone_like_contact_pay(contact_on_db)
        assert contact_on_home_page.all_email_contact == merge_email_like_contact_pay(contact_on_db)


def test_contact_phone_view(app):
    phone_on_home_page = app.contact.get_contacts_list()[0]
    phone_on_view_page = app.contact.get_contact_list_on_view_page(0)
    assert phone_on_home_page.home == phone_on_view_page.home
    assert phone_on_home_page.work_phone == phone_on_view_page.work_phone
    assert phone_on_home_page.mobile_phone == phone_on_view_page.mobile_phone
    assert phone_on_home_page.second_phone == phone_on_view_page.second_phone


def clear(str):
    return re.sub(bad_symbols, "", str)


def merge_phone_like_contact_pay(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.mobile_phone, contact.work_phone, contact.second_phone])
                         )
                     )
              )


def merge_email_like_contact_pay(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.email_1, contact.email_2, contact.email_3])
                         )
                     )
              )