# coding:utf-8
import socket
from handler.request import Request


class cloudProcess(Request):
    def post(self):
        vectors = self.get_argument('vectors')
        precious = self.get_argument('precious')
        headtotail = self.get_argument('headtotail')
        message = vectors + '|' + precious + '|' + headtotail
        serverHost = '192.168.0.16'
        serverPort = '45888'
        sockobj = socket(socket.AF_INET, socket.SOCK_STREAM)
        sockobj.connect((serverHost, serverPort))
        for line in message:
            # 经过套按字发送line至服务端
            sockobj.send(line)
            # 从服务端接收到的数据，上限为1k
            data = sockobj.recv(1024)
            # 确认他是引用的，是'x'
            print 'Client received:', repr(data)

        sockobj.close()
