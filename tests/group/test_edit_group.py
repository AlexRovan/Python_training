from model.group import Group
import random


def test_edit_group_by_index(app,json_groups):
    group = json_groups
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_groups_list()
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group,index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
