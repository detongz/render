# coding:utf-8
from handler.index import indexHandler, userIndexHandler
from handler.login import signupHandler, loginHandler, logOutHandler
from handler.error import errorHandler, errorHandler404

urls = [
    (r'/', indexHandler),  # 首页/查看全部作品
    (r'/login', loginHandler),  # 登陆界面
    (r'/logout', logOutHandler),  # 登陆界面
    (r'/signup', signupHandler),  # 申请新用户界面
    (r'/user', userIndexHandler),  # 用户界面首页
    # 处理错误
    (r'/error/(.*)/(.*)', errorHandler),  # 各类报错信息
    (r'/error/404', errorHandler),
    (r'/error/', errorHandler),
    (r".*", errorHandler404),
]
