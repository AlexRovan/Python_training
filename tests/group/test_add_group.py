# -*- coding: utf-8 -*-
from model.group import Group

group_1 = Group(name="group_name_1", header="group_header_1", footer="group_footer_1")
empty_group = Group(name="", header="", footer="")


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(group_1)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(empty_group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)




