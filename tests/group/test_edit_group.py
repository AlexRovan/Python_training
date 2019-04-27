from model.group import Group

group_edit = Group(name="group_edit_name_1", header="group_edit_header_1", footer="group_edit_footer_1")


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(group_edit)
    app.session.logout()
