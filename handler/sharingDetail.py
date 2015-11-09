# coding:utf-8
import os
import commands
from models.files import getCertainFile, getUploadType, removeSharedRecord
from handler.request import Request


class sharingDetailHandler(Request):
    # 查看分享详细信息
    def get(self, fid, *args, **kwargs):
        id = self.get_secure_cookie('id')
        info = getCertainFile(fid)

        self.render('detailShared.html', uid=id, info=info)


class shareDeleteHandler(Request):
    # 删除分享内容， url访问
    def get(self, fid):
        type = getUploadType(fid)

        # 验证身份，部分安全保障
        if self.get_secure_cookie('id') == type['id']:
            if type['type'] == 'mod':
                pathPic = os.path.dirname(__file__)[:-8] + '/static/imgshare'
                removeShared(pathPic, fid)  # 删除模型预览
                pathMod = '/tmp/share'
                removeShared(pathMod, fid)  # 删除模型文件
                removeSharedRecord(fid)
            elif type['type'] == 'pic':
                pathPic = os.path.dirname(__file__)[:-8] + '/static/imgshare'
                removeShared(pathPic, fid)  # 删除图片分享文件
                removeSharedRecord(fid)

        self.redirect('/user')


def removeShared(path, id):
    # 删除已经分享的文件
    # 删除本来存在的用户头像
    cmd = 'find ' + path + ' -name ' + id + '.*'
    print cmd
    fpath = commands.getstatusoutput(cmd)[1]
    cmd = 'rm ' + fpath
    print cmd
    os.system(cmd)