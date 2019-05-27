# -*- coding: utf-8 -*-
import pytest
import json
import os.path
from fixture.application import Application

fixture = None
target = None


@pytest.fixture()
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    if target is None:
        config_path =os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_path) as configfile:
            target = json.load(configfile)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser,target["baseUrl"])

    fixture.session.login_ensure(target["username"], target["password"])
    return fixture


@pytest.fixture(scope = "session",autouse = True)
def stop(request):

    def fin():
        fixture.session.logout_ensure()
        fixture.destroy()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
