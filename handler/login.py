# coding:utf-8

from handler.request import Request
from tornado.escape import json_encode
from handleInput import qn


class loginHandler(Request):
    """登录页面"""

    def get(self):
        self.render("login.html")

    def post(self, *args, **kwargs):
        uid = self.get_argument('id')
        pwd = self.get_argument('pwd')
        result = {}
        try:
            uid = qn(uid)
            result['result'] = 'success'
        except TypeError:
            result['result'] = 'login_username'
        try:
            pwd = qn(pwd)
        except TypeError:
            result['result'] = 'login_pwd',

        self.write(json_encode(result))


class signupHandler(Request):
    def get(self, *args, **kwargs):
        self.render('inner.html')
