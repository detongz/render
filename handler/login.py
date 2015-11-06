# coding:utf-8
from _mysql import IntegrityError

from handler.request import Request
from tornado.escape import json_encode
from handleInput import qn
from models.query import getUser, getUserById, signUp
import re


class loginHandler(Request):
    """登录页面"""

    def get(self):
        id = self.get_secure_cookie('id')
        if not id:
            self.render("login.html", uid=id)
        else:
            self.redirect('/')

    def post(self, *args, **kwargs):
        uid = self.get_argument('id')
        pwd = self.get_argument('pwd')
        result = {}
        try:
            uid = qn(uid)
            try:
                pwd = qn(pwd)
                if not getUser(uid, pwd):
                    result['result'] = 'no_such_user'
                else:
                    self.set_secure_cookie('id', uid)
                    result['result'] = 'success'
            except TypeError:
                result['result'] = 'login_pwd',
        except TypeError:
            result['result'] = 'login_username'

        self.write(json_encode(result))


class logOutHandler(Request):
    """退出登陆"""

    def get(self, *args, **kwargs):
        self.clear_cookie('id')
        self.redirect('/')


class signupHandler(Request):
    """用户注册"""

    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        if not id:
            self.render('signup.html', uid=id)
        else:
            self.redirect('/')

    def post(self, *args, **kwargs):
        result = {}
        id = self.get_argument('id')
        pwd = self.get_argument('pwd')
        email = self.get_argument('email')

        try:
            id = qn(id)
            pwd = qn(pwd)
            email = qn(email)
            if not getUserById(id):
                try:
                    signUp(id, pwd, email)
                    result['result'] = 'success'
                except IntegrityError:
                    result['result'] = 'email_existed'
            else:
                result['result'] = 'user_existed'
        except TypeError:
            result['result'] = 'special_marks'

        self.write(json_encode(result))


class changePersonalProfileHandler(Request):
    """用户修改个人信息"""

    def get(self, *args, **kwargs):
        pass