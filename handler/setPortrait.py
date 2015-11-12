# coding:utf-8
import os
from handler.request import Request
from handler.sharingDetail import removeShared
from models.query import getUserById, userSetPortrait


class setPortraitHandler(Request):
    # 设置个人头像
    def prepare(self):
        self.id = self.get_secure_cookie('id')

    def get(self, *args, **kwargs):
        if not self.id:
            self.redirect('/login')
        else:
            self.render('setPortrait.html', uid=self.id)

    def post(self, *args, **kwargs):
        try:
            f = self.request.files['sharefile'][0].body
            fname = self.request.files['sharefile'][0].filename
            ext = fname.split('.')[-1]

            if not self.id:
                self.redirect('/login')
            else:
                if ext not in ['jpg', 'jpeg', 'png', 'gif', 'JPEG', 'tiff', 'tif', 'raw']:
                    self.redirect('/error/sharePicError/')
                else:

                    if not getUserById(self.id):
                        self.redirect('/error/no_such_user/')
                    else:
                        # 保存文件
                        try:
                            path = os.path.dirname(__file__)[:-8] + '/static/portrait'

                            filename = self.id + '.' + ext

                            removeShared(path, self.id)

                            fpath = os.path.join(path, filename)
                            fi = open(fpath, 'w')
                            fi.write(f)
                            fi.close()
                            userSetPortrait('/static/portrait/' + filename, self.id)

                            self.redirect('/user')
                        except Exception as e:
                            print e
        except KeyError as e:
            pass
