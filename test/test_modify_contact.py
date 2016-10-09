# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email="666999@mail.ru"))
    app.session.logout()

def test_modify_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="666000"))
    app.session.logout()