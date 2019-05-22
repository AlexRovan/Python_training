# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.group import Group


def random_string(prefix,maxlen = 10):
    symbols = string.ascii_letters + string.punctuation + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
            Group(name=name, header=header, footer=footer)
            for name in ["", random_string("name_",10)]
            for header in ["", random_string("header_",20)]
            for footer in ["", random_string("footer_",20)]
            ]


@pytest.mark.parametrize("group",testdata, ids=[repr(x) for x in testdata])
def test_add_group(app,group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)





