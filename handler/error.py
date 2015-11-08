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
    'plsease_login': '要登陆才可以用的哦(●\'◡\'●)ﾉ♥',
    'shareModelError': '请上传使用3Drender导出的模型哦(●\'◡\'●)ﾉ♥',
    'sharePicError': '请上传单张图片哦(●\'◡\'●)ﾉ♥',
    'file_error': '分享出问题啦 再试试吧(￣▽￣)~\*',
    'please_select_file': '上传要选择文件哦 ╮(๑•́ ₃•̀๑)╭',
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
