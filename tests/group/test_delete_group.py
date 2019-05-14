# -*- coding: utf-8 -*-
from model.group import Group

empty_group = Group(name="", header="", footer="")


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    old_groups = app.group.get_groups_list()
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups