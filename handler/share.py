#!coding:utf-8
# /usr/bin/python
import os
import datetime
import random

from tornado.escape import json_encode
from handler.request import Request
from models.files import generatingfid, shareFile
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
        try:
            # 从form表单中读取数据
            platform = self.get_argument('platform')
            f = ''
            fname = ''

            # 生成模型id
            (fid, time) = generateFId()

            if platform == '0':
                f = self.request.files['sharefile'][0].body
                fname = self.request.files['sharefile'][0].filename
            elif platform == '1':
                f = self.get_argument('sharefile')
                fname = fid
            id = self.get_argument('id')

            if not getUserById(id):
                self.redirect('/error/no_such_user/share')

            # 保存文件
            path = os.path.dirname(__file__)[:-8] + '/share/'
            fpath = path + fname
            fi = open(fpath, 'w')
            fi.write(f)
            fi.close()

            # 解压并处理文件
            (naming, description) = unzip(path, fname, fid)

            # 增加分享的文件记录
            shareFile(fid, naming, description, '/share/' + fid + '.png', time, id)

            if platform == '0':
                self.redirect('/')
            elif platform == '1':
                self.write(json_encode({'result': 'success'}))
        except Exception as e:
            print e
            # self.write(json_encode({'result': 'fail!'}))


def generateFId():
    now = id = datetime.datetime.now()
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
    return id, now.strftime("%Y-%m-%d %H:%M:%S")


def unzip(path, fname, id):
    # 解压文件，把图片文件保存在工程目录的share文件夹下，模型文件放在/tmp/share文件夹下
    cmd = '''
        cd %s
        if [ ! -d "/tmp/share" ]; then
            mkdir /tmp/share
        fi
        cd /tmp/share
        mkdir temp-%s
        unzip %s -d temp-%s
        rm %s
        mv temp-%s/*.png %s/%s.png
        mv temp-%s/*.unimax %s.unimax
        ''' \
          % (path, id, path + fname, id, path + fname, id, path, id, id, id)
    os.system(cmd)
    f = open('/tmp/share/temp-' + id + '/' + fname.split('.')[0] + '.txt')
    line = f.readline()
    line = line.split('|')
    cmd = '''rm -rf %s/temp-%s''' % ('/tmp/share', id)
    os.system(cmd)
    return line[0], line[1]  # 返回用户定描述信息义的名称和


def removeShared(path, id):
    cmd = '''rm %s/%s.*''' % (path, id)
    os.system(cmd)
