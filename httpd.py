
import time
import socket
import threading

"""
socket编程思路
TCP服务端：
1 创建套接字，绑定套接字到本地IP与端口
   # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind()
2 开始监听连接                   #s.listen()
3 进入循环，不断接受客户端的连接请求              #s.accept()
4 然后接收传来的数据，并发送给对方数据         #s.recv() , s.sendall()
5 传输完毕后，关闭套接字                     #s.close()

TCP客户端:
1 创建套接字，连接远端地址
       # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.connect()
2 连接后发送数据和接收数据          # s.sendall(), s.recv()
3 传输完毕后，关闭套接字          #s.close()
"""

def log(*argv, **kwargs):
    """
    格式化输出
    """
    print(*argv, **kwargs)


def startup(host, port):
    """
    初始化服务器 socket
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 定义socket类型，网络通信，TCP
    s.bind((host, port))  # 套接字绑定的IP与端口
    s.listen(5)         # 开始TCP监听
    return s


def route_index():
    """
    主页的处理函数, 返回主页的响应
    """
    header = 'HTTP/1.x 200 VERY OK\r\nContent-Type: text/html\r\n'
    body = '<h1>Hello World</h1>'
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def accept_request(conn, addr):
    """
    处理客户端请求
    GET / HTTP/1.1
    Host: 127.0.0.1:40001
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.8
    7 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding: gzip, deflate, sdch, br
    Accept-Language: zh-CN,zh;q=0.8
    """
    print('thread is running', threading.current_thread().name)
    #while True:
    # print(conn, addr)
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if len(data) < 2:
            break
        # log('server data', data)

        r = route_index()
        conn.sendall(r)


def main():
    """
    开始函数，初始化 socket
    """
    server_socket = -1
    port = 40001
    host = '127.0.0.1'
    client_socket = -1

    server_socket = startup(host, port)

    while True:
        conn, addr = server_socket.accept()     #接受TCP连接，并返回新的套接字与IP地址
        print('Connected by', addr)

        # 接受TCP链接后，开一个线程处理
        t = threading.Thread(target=accept_request, args=(conn, addr, ))
        t.start()
    t.join()
    log('end threading')


if __name__ == '__main__':
    main()
