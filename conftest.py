# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application

fixture = None


@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    passpord = request.config.getoption("--password")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser,base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser,base_url)
    fixture.session.login_ensure(username="admin", password=passpord)
    return fixture


@pytest.fixture(scope = "session",autouse = True)
def stop(request):

    def fin():
        fixture.session.logout_ensure()
        fixture.destroy()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--password", action="store", default="secret")
