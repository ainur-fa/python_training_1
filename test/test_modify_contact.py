# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="346346343"))
    app.session.logout()

# def test_modify_contact_mobile(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.modify_first_contact(Contact(firstname="erhherwh", lastname="werhwerh", address="erherhewh", mobile="346346343", email="ergergerger34"))
#     app.session.logout()