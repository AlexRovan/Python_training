# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application


@pytest.fixture(scope="session", autouse=True)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
