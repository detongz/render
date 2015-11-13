#!coding:utf-8
# /usr/bin/python
import os
import datetime
import random
import commands

from handler.handleInput import text2Html, qndes
from tornado.escape import json_encode
from handler.request import Request
from models.files import generatingfid, shareFile, shareFileImg
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
        platform = self.get_argument('platform')

        if not self.get_secure_cookie('id') and platform == '0':
            self.redirect('/login')
        else:
            # 生成模型id
            (fid, time) = generateFId()

            f = self.request.files['sharefile'][0].body
            fname = self.request.files['sharefile'][0].filename
            id = self.get_argument('id')

            if not getUserById(id):
                self.redirect('/error/no_such_user/share')
            else:
                if fname.split('.')[-1] != 'zunimax':
                    self.redirect('/error/shareModelError/share')
                else:

                    try:
                        # 保存文件
                        path = os.path.dirname(__file__)[:-8] + '/static/imgshare'
                        fpath = path + fname
                        fi = open(fpath, 'w')
                        fi.write(f)
                        fi.close()

                        # 解压并处理文件
                        (naming, description) = unzip(path, fname, fid)

                        # 增加分享的文件记录
                        shareFile(fid, naming, description, '/static/imgshare/' + fid + '.png', time, id)

                        if platform == '0':
                            self.redirect('/')
                        elif platform == '1':
                            pass
                    except:
                        pass
                    finally:
                        self.write(json_encode({'result': 'success'}))


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
        cp %s %s
        mkdir temp-%s
        unzip %s -d temp-%s
        rm %s
        mv temp-%s/*.png %s/%s.png
        # mv temp-%s/*.unimax %s.unimax
        ''' \
          % (path, path + fname, id+'.zunimax', id, path + fname, id, path + fname, id, path, id, id, id)
    os.system(cmd)
    cmd = 'find /tmp/share/temp-' + id + ' -name "*.txt"'
    txt = commands.getstatusoutput(cmd)[1]
    f = open(txt)
    line = f.readline()
    line = line.split('|')
    cmd = '''rm -rf %s/temp-%s''' % ('/tmp/share', id)
    os.system(cmd)
    return line[0], line[1]  # 返回用户定描述信息义的名称和


class chooseWhichHandler(Request):
    # 选择要分享的文件类型
    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        if not id:
            self.redirect('/login')
        else:
            self.render('chooseWhich.html', uid=id)


class sharePictureHandler(Request):
    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        if not id:
            self.redirect('/login')
        else:
            self.render('sharePic.html', uid=id)

    def post(self):

        try:
            f = self.request.files['sharefile'][0].body
            fname = self.request.files['sharefile'][0].filename
            description = self.get_argument('description')
            picname = self.get_argument('name')
            id = self.get_argument('id')
            ext = fname.split('.')[-1]

            if not id:
                self.redirect('/login')
            else:
                if ext not in ['jpg', 'jpeg', 'png', 'gif', 'JPEG', 'tiff', 'tif', 'raw']:
                    self.redirect('/error/sharePicError/share')
                else:

                    if not getUserById(id):
                        self.redirect('/error/no_such_user/share')
                    else:
                        try:
                            description = qndes(description)
                            description = text2Html(description)  # 保存换行信息
                            picname = qndes(picname)

                            # 生成文件id
                            (fid, time) = generateFId()

                            # 保存文件
                            try:
                                path = os.path.dirname(__file__)[:-8] + '/static/imgshare'

                                filename = fid + '.' + ext
                                fpath = os.path.join(path, filename)
                                fi = open(fpath, 'w')
                                fi.write(f)
                                fi.close()
                                shareFileImg(fid, picname, description, '/static/imgshare/' + filename, time, id)

                                self.redirect('/user')
                            except Exception as e:
                                print e
                        except TypeError:
                            self.redirect('/error/special_marks/share')
        except KeyError as e:
            pass
