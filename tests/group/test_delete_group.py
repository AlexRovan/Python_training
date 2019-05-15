# -*- coding: utf-8 -*-
from model.group import Group
import random


empty_group = Group(name="", header="", footer="")


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    old_groups = app.group.get_groups_list()
    index = random.randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
