#!coding:utf-8
# /usr/bin/python
import os, datetime, random
from handler.request import Request
from models.files import generatingfid

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
            # 从form表单中读取数据
            f = self.request.files['sharefile'][0].body
            fname = self.request.files['sharefile'][0].filename
            naming = self.get_argument('naming')
            description = self.get_argument('description')
            path = os.path.dirname(__file__)[:-8] + '/share/'
            fpath=path + fname
            fi = open(fpath, 'w')
            fi.write(f)
            fi.close()

            # 解压并处理文件


            self.redirect('/')
        except Exception as e:
            print e
            self.redirect('/error/file_error/share')


def generateFId():
    while True:
        now = datetime.datetime.now()
        r = random.randint(0, 99)
        if r < 10:
            r = '0' + str(r)
        else:
            r = str(r)
        id = now.strftime('%f') + r
        if not generatingfid(id):
            break
    return id

def unzip(filepath):
    pass