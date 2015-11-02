# coding:utf-8

from handler.request import Request
from tornado.escape import json_encode
from handleInput import qn
from models.query import getUser


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
                    print uid
                    result['result'] = 'success'
            except TypeError:
                result['result'] = 'login_pwd',
        except TypeError:
            result['result'] = 'login_username'

        self.write(json_encode(result))


class logOutHandler(Request):
    def get(self, *args, **kwargs):
        self.clear_cookie('id')
        self.redirect('/')


class signupHandler(Request):
    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        if not id:
            self.render('signup.html', uid=id)
        else:
            self.redirect('/')

    def post(self, *args, **kwargs):
        id=self.get_argument('id')
        pwd=self.get_argument('pwd')
        email=self.get_argument('email')