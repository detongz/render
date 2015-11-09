# coding:utf-8
from handler.request import Request


class cloudProcess(Request):
    def post(self):
        vectors = self.get_argument('vectors')
        precious = self.get_argument('precious')
        headtotail = self.get_argument('headtotail')
        print vectors
        print precious
        print headtotail
