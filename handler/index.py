# coding:utf-8

import tornado.web
from models.query import getUserById
from models.files import getSharedModels, getSharedModelsById


class indexHandler(tornado.web.RequestHandler):
    """首页"""

    def get(self):
        shared = getSharedModels()
        id = self.get_secure_cookie('id')
        self.render("index.html", uid=id, sharing=shared)


class userIndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        if not id:
            self.redirect('/login')
        user = getUserById(id)
        shared = getSharedModelsById(id)
        self.render('userIndex.html', uid=id, user=user, sharing=shared)


class viewCertainUserHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        pass
