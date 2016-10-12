# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="erhherwh", lastname="werhwerh", address="erherhewh", mobile="346346343", email="ergergerger34"))

def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="", email=""))
