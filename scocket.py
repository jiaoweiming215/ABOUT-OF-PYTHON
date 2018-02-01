# format string

#-*-coding:utf-8-*-

###
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
客户端：主动发起连接的叫客户端，被动响应连接的叫服务器。
大多数连接都是可靠的TCP连接。
创建一个基于TCP连接的socket
###
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connet(('www.baidu.com',80))
