# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random

def test_del_contact_in_group(app, db, orm):
    list =[]
    app.contact.check_available_min_requirement(app, db)
    group_list = db.get_group_list()
    for this_group in group_list:
        contacts_in_group = orm.get_contacts_in_group(Group(id=this_group.id))
        [list.append(elem) for elem in contacts_in_group if elem not in list]

    if list ==[]:
        group = random.choice(db.get_group_list())
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id)
        list.append(orm.get_contact_list()[0])

    contact = random.choice(list)
    group =  random.choice(orm.get_group_where_contact(Contact(id=contact.id)))
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.del_contact_in_group(contact.id, group.id)
    new_contacts = orm.get_contacts_in_group(group)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
