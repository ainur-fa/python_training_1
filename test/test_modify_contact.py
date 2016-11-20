# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact
import random

def test_modify_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "tester",email="test@test", mobilephone = "911"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact_data = Contact(firstname="Test666999")
    app.contact.modify_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for x in range(len(old_contacts)):
        if old_contacts[x].id == contact.id:
            index = x
    old_contacts[index].firstname = new_contact_data.firstname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# def test_modify_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname = "tester", email="test@test", mobile = "911"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(mobile="666000"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
