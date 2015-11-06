# coding:utf-8

import torndb

db = torndb.Connection('localhost', 'renderServer', 'root')


def signup(id, password, email):
    sql = '''insert into user (%s,%s,%s) values ('1','1','q@q.com');''' % (id, password, email)
    db.execute(sql)


def setUserImage(id, fname):
    sql = '''update user set image='/static/images/preview/%s' where id='%s';''' % (fname, id)
    db.execute(sql)


def setUserDescription(id, description):
    sql = '''update user set description='%s' where id='%s';''' % (description, id)
    db.execute(sql)


def getUser(id, pwd):
    # 用户登录
    sql = '''select * from user where id="%s" and password="%s";''' % (id, pwd)
    r = db.query(sql)
    if not r:
        return None
    else:
        return r[0]


def getUserById(id):
    # 用户名是否已经存在
    # 获取某用户所有信息
    sql = '''select * from user where id="%s";''' % (id)
    r = db.query(sql)
    if not r:
        return None
    else:
        return r[0]


def signUp(id, pwd, email):
    # 新用户注册
    sql = '''insert into user (id,password,email) values ('%s','%s','%s');''' % (id, pwd, email)
    db.execute(sql)


if __name__ == "__main__":
    id = raw_input()
    pwd = raw_input()
    print getUser(id, pwd)
