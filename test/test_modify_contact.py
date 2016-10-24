# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "tester",email="test@test", mobile = "911"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test666999")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname = "tester", email="test@test", mobile = "911"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(mobile="666000"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
