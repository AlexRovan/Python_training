# -*- coding: utf-8 -*-
import pytest

from application import Application
from contact import Contcat

father = Contcat("Alex", "Rovan", "CFT", "Novosibirsk", "123321321", "12331223", "413243243", "weqwwe@sffse.ri")
empty = Contcat("", "", "", "", "", "", "", "")


@pytest.fixture
def app (request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(father)
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.create_contact(empty)
    app.logout()







