# -*- coding: utf-8 -*-

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()