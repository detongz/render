# coding:utf-8

import tornado.web
from models.query import getUserById


class indexHandler(tornado.web.RequestHandler):
    """首页"""

    def get(self):
        id = self.get_secure_cookie('id')
        self.render("index.html", uid=id)


class userIndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        user = getUserById(id)
        self.render('userIndex.html', uid=id, user=user)


class viewCertainUserHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        pass