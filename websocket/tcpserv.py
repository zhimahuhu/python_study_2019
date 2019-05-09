# -*- coding:utf-8 -*-
# @Time   : 2019/5/9 22:45
# @Author : lukazhou

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('-----')
    tcpclient, addr = tcpSerSock.accept()
    receivedData = str(tcpclient.recv(2048))
    body='''<!DOCTYPE html>
<html>
<body>

<h1>'''+receivedData+''''</h1>

<p>我的第一个段落。</p>

</body>
</html>'''
    data = ("""HTTP/1.1 200 OK
Date: Sat, 31 Dec 2005 23:59:59 GMT
Content-Type: text/html;charset=utf-8

%s

""" % body).encode('utf-8')
    tcpclient.send(bytes(data))
tcpSerSock.close()