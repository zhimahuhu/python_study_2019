# -*- coding:utf-8 -*-
# @Time   : 2019/5/9 17:45
# @Author : lukazhou

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

addr_list = []

while True:
    print('wating for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    addr_list.append(addr)
    for i in addr_list:
        udpSerSock.sendto(data, i)
    print('...received from and returned to:', addr)
udpSerSock.close()