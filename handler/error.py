# coding:utf-8
from handler.request import Request

error_info = {
    'login_username': '昵称中不要包含特殊符号哦 ～≥▽≤～',
    'login_pwd': '密码中不要包含特殊符号哦 ～≥▽≤～',
    '404': '页面找不到啦~\(≧▽≦)/~',
    'no_such_user': '这个昵称可能没有注册过哦(⊙o⊙)',
}


class errorHandler(Request):
    """渲染各类错误消息"""

    def get(self, error_type='404', selecting=None):
        if not selecting:
            self.render('error.html', uid=id, selecting=selecting, error_info=error_info[error_type])


class errorHandler404(Request):
    """专门处理错误信息"""

    def get(self, *args, **kwargs):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', uid=id, selecting=404, error_info=None)
