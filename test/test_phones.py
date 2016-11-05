import re
from random import randrange

def test_phones_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_fields_like_on_home_page(contact_from_edit_page, type="phones")
    assert contact_from_home_page.all_emails_from_home_page == merge_fields_like_on_home_page(contact_from_edit_page, type="emails")
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
        return re.sub("[() -]","", s)

def merge_fields_like_on_home_page(contact, type):
    if type == "phones": merged = [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]
    elif type == "emails": merged = [contact.email, contact.email2, contact.email3]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, merged))))
