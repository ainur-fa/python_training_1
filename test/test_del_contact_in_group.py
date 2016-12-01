# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root",password="")
import random
import time

def test_del_contact_in_group(app, db):
    app.contact.check_available_min_requirement(app, db)
    list =[]
    group_list = db.get_group_list()
    for this_group in group_list:
        contacts_in_group = db_orm.get_contacts_in_group(Group(id=this_group.id))
        [list.append(elem) for elem in contacts_in_group if elem not in list]
    if list ==[]:
        group = random.choice(db.get_group_list())
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.name)
        list.append(db_orm.get_contact_list()[0])

    contact = random.choice(list)
    group =  random.choice(db_orm.get_group_where_contact(Contact(id=contact.id)))
    app.contact.del_contact_in_group(contact.id, group.id)
    assert contact not in db_orm.get_contacts_in_group(Group(id=group.id))