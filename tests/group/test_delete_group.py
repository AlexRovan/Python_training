# -*- coding: utf-8 -*-
from model.group import Group

empty_group = Group(name="", header="", footer="")


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    app.group.delete_first_group()



