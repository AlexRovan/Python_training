# -*- coding: utf-8 -*-


def test_delete_group(app):
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()


