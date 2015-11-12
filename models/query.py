# coding:utf-8


import torndb

db = torndb.Connection('localhost', 'renderServer', 'root')

"""针对用户进行操作的部分"""


def setUserImage(id, fname):
    # 修改用户头像
    # 未实现！！！
    sql = '''update user set image='/static/images/preview/%s' where id='%s';''' % (fname, id)
    db.execute(sql)


def setUserDescription(id, description):
    # 修改用户自我介绍
    # 未实现！！！
    sql = '''update user set description='%s' where id='%s';''' % (description, id)
    db.execute(sql)


def getUser(id, pwd):
    # 用户登录
    sql = '''select * from user where id="%s" and password="%s";''' % (id, pwd)
    print sql
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


def signUp(id, pwd, email, desc):
    # 新用户注册
    if desc != '':
        sql = '''insert into user (id,password,email,description) values ('%s','%s','%s','%s');''' % (
            id, pwd, email, desc)
    else:
        sql = '''insert into user (id,password,email) values ('%s','%s','%s');''' % (id, pwd, email)
    db.execute(sql)


def userSetPortrait(path, id):
    # 用户设置/更新头像
    sql = "update user set image='%s' where id='%s';" % (path, id)
    db.execute(sql)


def userSetPortrait(description, id):
    # 用户设置/更新个人信息
    sql = "update user set description='%s' where id='%s';" % (description, id)
    db.execute(sql)


if __name__ == "__main__":
    id = raw_input()
    pwd = raw_input()
    print getUser(id, pwd)
