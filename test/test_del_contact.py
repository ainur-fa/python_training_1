# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact
import random
import pytest

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="tester", email="test@test", mobilephone="911"))
    with pytest.allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with pytest.allure.step("When get random contact"):
        contact = random.choice(old_contacts)
    with pytest.allure.step("When I delete %s" % contact):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step("Then the new contact list is equal to the old list with the deleted contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)