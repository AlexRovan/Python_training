# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contcat

father = Contcat("Alex", "Rovan", "CFT", "Novosibirsk", "123321321", "12331223", "413243243", "weqwwe@sffse.ri")
empty = Contcat("", "", "", "", "", "", "", "")


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(father)
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(empty)
    app.session.logout()







