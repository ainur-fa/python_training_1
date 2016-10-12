# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "tester",email="test@test", mobile = "911"))
    app.contact.modify_first_contact(Contact(email="666999@mail.ru"))

def test_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "tester", email="test@test", mobile = "911"))
    app.contact.modify_first_contact(Contact(mobile="666000"))
