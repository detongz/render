#!coding:utf-8
# /usr/bin/python
import os
from tornado.escape import json_encode
from handler.request import Request


class shareHandler(Request):
    """模型分享 网页端"""

    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        if not id:
            self.redirect('/error/plsease_login/share')
        else:
            self.render('share.html', uid=id)

    def post(self, *args, **kwargs):
        """解析来自web端post请求"""
        try:
            f = self.request.files['sharefile'][0].body
            fname = self.request.files['sharefile'][0].filename
            description = self.get_argument('description')
            path = os.path.dirname(__file__)[:-8] + '/share/'
            fi = open(path + fname, 'w')
            fi.write(f)
            fi.close()
            self.redirect('/')
        except Exception as e:
            print e
            self.redirect('/error/file_error/share')
