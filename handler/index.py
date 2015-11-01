# coding:utf-8

import tornado.web
from tornado.escape import json_encode


class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class signupHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self, *args, **kwargs):
        uid = self.get_argument('id')
        pwd = self.get_argument('pwd')
        result = {'result': 'success'}
        self.write(json_encode(result))


class userIndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('success')
