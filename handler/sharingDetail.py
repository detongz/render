# coding:utf-8
import os
import commands
from models.files import getCertainFile, getUploadType
from handler.request import Request


class sharingDetailHandler(Request):
    def get(self, fid, *args, **kwargs):
        id = self.get_secure_cookie('id')
        info = getCertainFile(fid)

        self.render('detailShared.html', uid=id, info=info)


class shareDeleteHandler(Request):
    def get(self, fid):
        type = getUploadType(fid)
        if self.get_secure_cookie('id') == type['id']:
            if type['type'] == 'mod':
                pathPic = os.path.dirname(__file__)[:-8] + '/static/imgshare'
                removeShared(pathPic, fid)
                pathMod = '/tmp/share'
                removeShared(pathMod, fid)
            elif type['type'] == 'pic':
                pathPic = os.path.dirname(__file__)[:-8] + '/static/imgshare'
                removeShared(pathPic, fid)

        self.redirect('/user')


def removeShared(path, id):
    # 删除已经分享的文件
    cmd = 'find ' + path + ' -name ' + id + '.*'
    print cmd
    fpath = commands.getstatusoutput(cmd)[1]
    cmd = 'rm ' + fpath
    print cmd
    os.system(cmd)
