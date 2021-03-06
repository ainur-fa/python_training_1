# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group
import random
import pytest

def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    with pytest.allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with pytest.allure.step("When I get random group"):
        group = random.choice(old_groups)
    new_group_data = Group(name="New group")
    with pytest.allure.step("When I'm modify group %s" % group):
        app.group.modify_group_by_id(group.id, new_group_data)
    with pytest.allure.step("Then the new group list is equal to the old list with the modified group"):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        for x in range(len(old_groups)):
            if old_groups[x].id == group.id:
                index = x
        old_groups[index].name = new_group_data.name
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#
# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name = "test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
