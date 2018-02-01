# format string

#-*-coding:utf-8-*-

###
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
客户端：主动发起连接的叫客户端，被动响应连接的叫服务器。
大多数连接都是可靠的TCP连接。
创建一个基于TCP连接的socket
###
import socket
#AF_INET指定使用IPv4协议，如果使用IPv6，就指定为AF_INET6；SOCK_STREAM指定面向流的TCP协议，这样，一个socket对象就创建成功，但是还没有连接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#客户端主动发起TCP连接，需要知道服务器IP和端口号，新浪网站的IP可以用域名“www.sina.com.cb”自动转到IP地址，怎么知道网站的端口号呢？
#：作为服务器，提供什么样的服务，端口号必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定为80端口，因为
#80端口是WEB服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标
#准服务的端口，端口号大于1024的，可以任意使用。
s.connect(('www.baidu.com',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

