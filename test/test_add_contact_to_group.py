# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import time
from fixture.orm import ORMFixture
db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root",password="")

import random

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="tester", email="test@test", mobilephone="911"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    group = random.choice(db.get_group_list())
    contacts_not_in_group = db_orm.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact.id, group.name)
    contacts_in_group = db_orm.get_contacts_in_group(Group(id=group.id))
    assert contact in contacts_in_group
