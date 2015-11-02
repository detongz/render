# coding:utf-8
from handler.request import Request
error_info = {'login_username': '用户名中不要包含特殊符号哦～', 'login_pwd': '密码中不要包含特殊符号哦～', '404': '页面找不到啦~\(≧▽≦)/~'}


class errorHandler(Request):
    """渲染各类错误消息"""

    def get(self, error_type='404', selecting=None):
        self.render('error.html', selecting=selecting, error_info=error_info[error_type])
