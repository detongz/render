# coding:utf-8
import tornado.web


class Request(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', selecting=404,error_info=None)
