# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email="666999@mail.ru"))

def test_modify_contact_mobile(app):
    app.contact.modify_first_contact(Contact(mobile="666000"))
