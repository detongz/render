# coding:utf-8

import tornado.web


class indexHandler(tornado.web.RequestHandler):
    """首页"""

    def get(self):
        id = self.get_secure_cookie('id')
        self.render("index.html", uid=id)


class userIndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('/')
