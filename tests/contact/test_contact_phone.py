import re
import random


bad_symbols = "() -"


def test_compare_contact_edit_and_home(app):

    index = random.randrange(app.contact.count())
    contact_on_home_page = app.contact.get_contacts_list()[index]
    contact_on_edit_page = app.contact.get_contact_list_on_edit_page(index)

    assert contact_on_home_page.firstname == contact_on_edit_page.firstname
    assert contact_on_home_page.lastname == contact_on_edit_page.lastname
    assert contact_on_home_page.address == contact_on_edit_page.address
    assert contact_on_home_page.all_phone_contact == merge_phone_like_contact_pay(contact_on_edit_page)
    assert contact_on_home_page.all_email_contact == merge_email_like_contact_pay(contact_on_edit_page)


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