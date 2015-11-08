# coding:utf-8

from models.files import getCertainFile
from handler.request import Request


class sharingDetailHandler(Request):
    def get(self, fid, *args, **kwargs):
        id = self.get_secure_cookie('id')
        self.render('inner.html', uid=id)
