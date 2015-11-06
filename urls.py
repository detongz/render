# coding:utf-8
from handler.index import indexHandler, userIndexHandler, viewCertainUserHandler
from handler.login import signupHandler, loginHandler, logOutHandler, changePersonalProfileHandler
from handler.error import errorHandler, errorHandler404
from handler.share import shareHandler

urls = [
    (r'/', indexHandler),  # 首页/查看全部作品
    (r'/login', loginHandler),  # 登陆界面
    (r'/logout', logOutHandler),  # 登陆界面
    (r'/signup', signupHandler),  # 申请新用户界面
    (r'/user', userIndexHandler),  # 用户界面首页
    (r'/user/(.*)', viewCertainUserHandler),  # 用户界面首页
    (r'/share', shareHandler),  # 用户模型分享
    (r'/changeprofile', changePersonalProfileHandler),  # 用户模型分享
    # 处理错误
    (r'/error/(.*)/(.*)', errorHandler),  # 各类报错信息， 参数2为需要标记选择的部分
    (r'/error/(.*)', errorHandler),  # 各类报错信息
    (r'/error/404', errorHandler),
    (r'/error/', errorHandler),
    (r".*", errorHandler404),
]
