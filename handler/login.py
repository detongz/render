# coding:utf-8
from _mysql import IntegrityError

from handler.request import Request
from tornado.escape import json_encode
from handleInput import qn, qndes, text2Html, html2Text
from models.query import getUser, getUserById, signUp, userSetPortrait
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
        desc = self.get_argument('description')

        try:
            id = qn(id)
            pwd = qn(pwd)
            email = qn(email)
            desc = qndes(desc)
            if desc != '':
                desc = text2Html(desc)
            if not getUserById(id):
                try:
                    signUp(id, pwd, email, desc)
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

    def prepare(self):
        self.id = self.get_secure_cookie('id')

    def get(self, *args, **kwargs):
        if not self.id:
            self.redirect('/')
        else:
            user = getUserById(self.id)
            self.render('changeProfile.html', uid=self.id, user=user, descrip=html2Text(user['description']))

    def post(self, *args, **kwargs):
        email = self.get_argument('email')
        description = self.get_argument('description')
        if not getUserById(self.id):
            self.redirect('/error/no_such_user')
        else:
            try:
                description = qndes(description)
                description = text2Html(description)  # 保存换行信息
                email = qn(email)

                userSetPortrait(email, description, self.id)
                self.redirect('/user')
            except TypeError:
                self.redirect('/error/special_marks/share')
