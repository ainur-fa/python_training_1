# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="erhherwh", lastname="werhwerh", address="erherhewh", mobile="346346343", email="ergergerger34"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="", email=""))
    app.session.logout()
