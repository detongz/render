#!coding:utf-8
# /usr/bin/python
import os
import datetime
import random

from tornado.escape import json_encode
from handler.request import Request
from models.files import generatingfid
from models.query import getUserById


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
        # try:
            # 从form表单中读取数据
        f = self.request.files['sharefile'][0].body
        fname = self.request.files['sharefile'][0].filename
        id = self.get_argument('id')
        platform = self.get_argument('platform')

        if not getUserById(id):
            self.redirect('/error/no_such_user/share')

        # 保存文件
        path = os.path.dirname(__file__)[:-8] + '/share/'
        fpath = path + fname
        fi = open(fpath, 'w')
        fi.write(f)
        fi.close()

        fid = generateFId()  # 生成模型id
        # 解压并处理文件
        (naming, descriptionun) = unzip(path, fname, fid)

        if platform == '0':
            self.redirect('/')
        elif platform == '1':
            self.write(json_encode({'result': 'success'}))
        # except Exception as e:
        #     print e


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


def unzip(path, fname, id):
    cmd = '''cd %s
            mkdir temp-%s
            unzip %s -d temp-%s
            rm %s
            mv temp-%s/*.png %s.png
            mv temp-%s/*.unimax %s.unimax
            ''' \
          % (path, id, fname, id, fname, id, id, id, id)
    os.system(cmd)
    f = open(path + '/temp-' + id + '/' + fname.split('.')[0] + '.txt')
    line = f.readline()
    line = line.split('|')
    cmd = '''rm -rf %s/temp-%s''' % (path, id)
    os.system(cmd)
    return line[0], line[1]


def removeShared(path, id):
    cmd = '''rm %s/%s.*''' % (path, id)
    os.system(cmd)
