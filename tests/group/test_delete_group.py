# -*- coding: utf-8 -*-
import random
from data.group import empty_group
from model.group import Group
import allure

def test_delete_group_by_index(app, db, check_ui):
    with allure.step('Add group, if no groups now'):
        if len(db.get_group_list()) == 0:
            app.group.create(empty_group)
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('Delete random Group'):
        group = random.choice(old_groups)
        app.group.delete_group_by_id(group.id)
    with allure.step('Group removed'):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_groups_list(), key= Group.id_or_max)
