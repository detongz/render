# coding:utf-8
from handler.request import Request

error_info = {
    'login_username': '昵称中不要包含特殊符号哦 ～≥▽≤～',
    'login_pwd': '密码中不要包含特殊符号哦 ～≥▽≤～',
    'special_marks': '不要包含特殊符号哦&nbsp;(●\'◡\'●)ﾉ♥',
    '404': '页面找不到啦~\(≧▽≦)/~',
    'no_such_user': '用户名或密码有问题哦(⊙o⊙)',
    'user_existed': '这个昵称已经被注册过了(⊙o⊙)',
    'email_existed': '这个邮箱已经被注册过了(⊙o⊙)',
}


class errorHandler(Request):
    """渲染各类错误消息"""

    def get(self, error_type='404', selecting=None):
        id = self.get_secure_cookie('id')
        self.render('error.html', uid=id, selecting=selecting, error_info=error_info[error_type])


class errorHandler404(Request):
    """专门处理错误信息"""

    def get(self, *args, **kwargs):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            id = self.get_secure_cookie('id')
            self.render('error.html', uid=id, selecting=404, error_info=None)
