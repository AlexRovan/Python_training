from model.group import Group

empty_group = Group(name="", header="", footer="")
group_edit = Group(name="group_edit_name_1", header="group_edit_header_1", footer="group_edit_footer_1")
group_edit_name = Group(name="group_edit_only_name_1")
group_edit_header = Group(header="group_edit_only_header_1")


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    app.group.edit_first_group(group_edit)


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    app.group.edit_first_group(group_edit_name)


def test_edit_header_first_group(app):
    if app.group.count() == 0:
        app.group.create(empty_group)
    app.group.edit_first_group(group_edit_header)