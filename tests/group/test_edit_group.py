from model.group import Group
import random
import allure

def test_edit_group_by_index(app,db,json_groups,check_ui):
    with allure.step('Add group, if no groups now'):
        group = json_groups
        if app.group.count() == 0:
            app.group.create(group)
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('Modify random Group'):
        group_edit = random.choice(old_groups)
        group.id = group_edit.id
        app.group.edit_group_by_id(group,group_edit.id)
    with allure.step('Group modified'):
        new_groups = db.get_group_list()
        old_groups.remove(group_edit)
        old_groups.append(group)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_groups_list(), key= Group.id_or_max)