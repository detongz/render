# coding:utf-8
import tornado.web
from handler.index import indexHandler, signupHandler, userIndexHandler

urls = [
    (r'/', indexHandler),
    (r'/login', signupHandler),
    (r'/user', userIndexHandler),
]
