# coding:utf-8
import base64
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from handler.request import Request
from models.query import getUserById
from models.files import getSharedModels, getSharedModelsById


class indexHandler(Request):
    """首页"""

    def get(self):
        shared = getSharedModels()
        id = self.get_secure_cookie('id')
        self.render("index.html", uid=id, sharing=shared)


class userIndexHandler(Request):
    """用户个人首页"""

    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        if not id:
            self.redirect('/login')
        user = getUserById(id)
        shared = getSharedModelsById(id)
        self.render('userIndex.html', uid=id, user=user, sharing=shared)


class viewCertainUserHandler(Request):
    # 查看特定用户的资料
    def get(self, tid, *args, **kwargs):
        id = self.get_secure_cookie('id')
        tid = base64.decodestring(tid)

        user = getUserById(tid)
        shared = getSharedModelsById(tid)
        self.render('userDetail.html', uid=id, user=user, sharing=shared)
