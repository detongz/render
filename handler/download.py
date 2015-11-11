# coding:utf-8
import os
import commands
from handler.request import Request


class downloadHandler(Request):
    # 分享‘模型’下载
    def get(self, fid, *args, **kwargs):
        path = commands.getoutput('find /tmp/share -name "'+fid+'".*')
        filename = path.split('/')[-1]
        x = open(path)
        self.set_header('Content-Type', 'text/csv')
        self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        self.finish(x.read())

class downloadPicHandler(Request):
    # 分享‘图片’下载
    def get(self, fid, *args, **kwargs):
        findpath = os.path.dirname(__file__)[:-8] + '/static/imgshare'
        path = commands.getoutput('find '+findpath+' -name "'+fid+'".*')
        filename = path.split('/')[-1]
        x = open(path)
        self.set_header('Content-Type', 'text/csv')
        self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        self.finish(x.read())
