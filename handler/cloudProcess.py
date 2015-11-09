# coding:utf-8
from handler.request import Request


class cloudProcess(Request):
    def post(self):
        self.get_argument('vectors')
        self.get_argument('precious')
        self.get_argument('headtotail')