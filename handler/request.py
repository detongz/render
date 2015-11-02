# coding:utf-8
import tornado.web


class Request(tornado.web.RequestHandler):
    """基类"""

    def __init__(self, application, request, **kwargs):
        super(Request, self).__init__(application, request, **kwargs)