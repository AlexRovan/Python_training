# -*- coding: utf-8 -*-
import random
from data.group import empty_group

def test_delete_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    old_groups = app.group.get_groups_list()
    index = random.randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
