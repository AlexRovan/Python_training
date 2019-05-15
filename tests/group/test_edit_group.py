from model.group import Group
import random

empty_group = Group(name="", header="", footer="")
group_edit = Group(name="group_edit_name_1", header="group_edit_header_1", footer="group_edit_footer_1")
group_edit_name = Group(name="group_edit_only_name_1")
group_edit_header = Group(header="group_edit_only_header_1")


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    old_groups = app.group.get_groups_list()
    index = random.randrange(len(old_groups))
    group_edit.id = old_groups[index].id
    app.group.edit_group_by_index(group_edit,index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = group_edit
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


#def test_edit_name_first_group(app):
#    if app.group.count() == 0:
#        app.group.create(empty_group)
#    old_groups = app.group.get_groups_list()
#    app.group.edit_first_group(group_edit_name)
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) == len(new_groups)


#def test_edit_header_first_group(app):
#    if app.group.count() == 0:
#        app.group.create(empty_group)
#    old_groups = app.group.get_groups_list()
#    app.group.edit_first_group(group_edit_header)
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) == len(new_groups)