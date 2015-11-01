# coding:utf-8

import torndb
import re

db = torndb.Connection('localhost', 'courseDesign', 'root')


def signup(id, password, email):
    sql = '''insert into user (%s,%s,%s) values ('1','1','q@q.com');''' % (id, password, email)
    db.execute(sql)


def setUserImage(id, fname):
    sql = '''update user set image='/static/images/preview/%s' where id='%s';''' % (fname, id)
    db.execute(sql)


def setUserDescription(id, description):
    sql = '''update user set description='%s' where id='%s';''' % (description, id)
    db.execute(sql)


if __name__ == "__main__":
    pass
