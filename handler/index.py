# coding:utf-8

import tornado.web


class indexHandler(tornado.web.RequestHandler):
    """首页"""
    def get(self):
        self.render("index.html")


class userIndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('success')
