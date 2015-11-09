# coding:utf-8

from models.files import getCertainFile
from handler.request import Request


class sharingDetailHandler(Request):
    def get(self, fid, *args, **kwargs):
        id = self.get_secure_cookie('id')
        info = getCertainFile(fid)

        self.render('detailShared.html',uid=id,info=info)
