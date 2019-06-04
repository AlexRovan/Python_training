# -*- coding: utf-8 -*-
import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.application import Application
from fixture.db import DB_fixture

fixture = None
target = None


@pytest.fixture()
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    target = load_config(request.config.getoption("--target"))
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser,target["web"]["baseUrl"])

    fixture.session.login_ensure(target["web"]["username"], target["web"]["password"])
    return fixture

@pytest.fixture(scope= "session")
def db (request):
    target=load_config(request.config.getoption("--target"))["db"]
    db_fixture = DB_fixture(target["host"],target["database"],target["user"],target["password"])
    def fin():
        db_fixture.destroy()
    request.addfinalizer(fin)
    return db_fixture

@pytest.fixture()
def check_ui(request):
    return request.config.getoption("--check_ui")

@pytest.fixture(scope = "session",autouse = True)
def stop(request):

    def fin():
        fixture.session.logout_ensure()
        fixture.destroy()

    request.addfinalizer(fin)

def load_config(file):
    global target
    if target is None:
        config_path =os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_path) as configfile:
            target = json.load(configfile)
    return target

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
    parser.addoption("--check_ui", action="store_true")
