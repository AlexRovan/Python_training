# -*- coding: utf-8 -*-
import pytest
import json
import jsonpickle
import os.path
import importlib
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

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata,ids=[repr(x) for x in testdata])

def load_from_module(name):
    return importlib.import_module("data.%s" % name).testdata

def load_from_json(name):
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data/%s.json" % name)
    with open(data_path) as f:
        return jsonpickle.decode(f.read())


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
