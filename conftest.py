# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application

fixture = None


@pytest.fixture()
def app():
    global fixture

    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()

    fixture.session.login_ensure(username="admin", password="secret")
    return fixture


@pytest.fixture(scope = "session",autouse = True)
def stop(request):

    def fin():
        fixture.session.logout_ensure()
        fixture.destroy()

    request.addfinalizer(fin)


