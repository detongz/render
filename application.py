# coding:utf-8
import os
import tornado.web
from urls import urls


class application(tornado.web.Application):
    def __init__(self):
        setting = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug="True",
            cookie_secret="e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            login_url="/login",
        )
        handlers = urls
        tornado.web.Application.__init__(self, handlers, **setting)