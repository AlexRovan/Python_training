# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group

group_1 = Group(name="group_name_1", header="group_header_1", footer="group_footer_1")
empty_group = Group(name="", header="", footer="")


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(group_1)
        app.logout()


def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(empty_group)
        app.logout()




